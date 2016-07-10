from django.db import models, connection
from django.utils import timezone
from .db_utils import execute_raw_query
from datetime import timedelta
WAIT_TIME = timedelta(seconds=20, minutes=0)

class TagTrackerManager(models.Manager):
    def update_tag_location(self, tag_id, antenna, reader, found_time):
      tags = self.raw(
          """
          select t.* from tag_metrics_tagtracker t
          where t.tag_id=%(tag_id)s
          order by t.id desc limit 1;
          """
          , {'tag_id': tag_id}
      )
      tags = list(tags)
      if tags:
        prev_tag = tags[0]
        same_location = reader == prev_tag.reader
        if same_location:
          time_diff = found_time - prev_tag.updated_time
          if time_diff > WAIT_TIME:
            # print 'Toggling status in same reader'
            self.create_tag_tracker(tag_id, antenna, reader, 
                1 - prev_tag.status, found_time, found_time)
          else:
            # print 'Updating time in same reader'
            prev_tag.updated_time = found_time
            prev_tag.save()
        else:
            # print 'Creating record for new reader for existing tag'
            self.create_tag_tracker(tag_id, antenna, reader, 
                self.model.STATUS_IN, found_time, found_time)
      else:
            # print 'Creating record for new reader for new tag'
            self.create_tag_tracker(tag_id, antenna, reader, 
                self.model.STATUS_IN, found_time, found_time)

    def create_tag_tracker(self, tag_id, antenna, reader, status, created_time=None, updated_time=None):
      if not created_time:
        created_time = timezone.now()
      if not updated_time:
        updated_time = timezone.now()
      tag_tracker = self.model(
          tag_id=tag_id,
          antenna=antenna,
          reader=reader,
          status=status,
          created_time=created_time,
          updated_time=updated_time
      )
      tag_tracker.save()
      return tag_tracker

    def last_locations(self):
        tags = self.raw(
            """
            select t.*, s.store from tag_metrics_tagtracker t
            inner join tag_metrics_storereader s on s.reader = t.reader
            where t.id in (
                select max(t1.id) from tag_metrics_tagtracker t1 group by tag_id
            )
            and s.status = 1
            order by s.store;
            """
        )
        return tags

    def store_stock(self):
        query = """
            select count(t.tag_id) as stock, s.store from tag_metrics_tagtracker t
            inner join tag_metrics_storereader s on s.reader = t.reader
            where t.id in (
                select max(t1.id) from tag_metrics_tagtracker t1 group by tag_id
            )
            and s.status = 1
            group by s.store
            order by s.store;
            """
        return execute_raw_query(query, None, 'store_stock')

    def tag_flow(self, start_date, end_date):
        query = """
            select s.store, a.in_flow, b.out_flow from
            (select reader, flow as in_flow from
            (select reader, count(id) as flow from tag_metrics_tagtracker
            where updated_time between %(start_date)s and %(end_date)s
            and status = 1
            group by reader
            ) c) a
            inner join
            (select reader, flow as out_flow from
            (select reader, count(id) as flow from tag_metrics_tagtracker
            where updated_time between %(start_date)s and %(end_date)s
            and status = 0
            group by reader
            ) d) b on a.reader = b.reader
            inner join tag_metrics_storereader s on s.reader = a.reader;
            """
        params = {'start_date': start_date, 'end_date': end_date}
        return execute_raw_query(query, params, 'tag_flow')


class TagTracker(models.Model):
    tag_id = models.CharField(max_length=1024, null=False)
    antenna = models.CharField(max_length=1024, null=False)
    reader = models.CharField(max_length=1024, null=False)
    status = models.IntegerField(null=False)
    created_time = models.DateTimeField(null=False)
    updated_time = models.DateTimeField(null=False)
    objects = TagTrackerManager()

    STATUS_OUT = 0
    STATUS_IN = 1

    def __str__(self):
        return str(self.__dict__)

class StoreReader(models.Model):
    store = models.CharField(max_length=1024, null=False)
    reader = models.CharField(max_length=1024, null=False)
    status = models.IntegerField(null=False)
    created_time = models.DateTimeField(null=False)
    updated_time = models.DateTimeField(null=False)

    def __str__(self):
        return str(self.__dict__)

