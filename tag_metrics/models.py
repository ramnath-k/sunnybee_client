from django.db import models, connection
from django.utils import timezone
from .db_utils import execute_raw_query

class TagTrackerManager(models.Manager):
    def create_tag_tracker(self, tag_id, antenna, reader, status):
        tag_tracker = self.model(
            tag_id=tag_id,
            antenna=antenna,
            reader=reader,
            status=status,
            created_time=timezone.now(),
            updated_time=timezone.now()
        )
        tag_tracker.save()
        return tag_tracker

    def last_locations(self):
        tags = self.raw(
            """
            select t.*, s.store from tag_tracker t
            inner join store_reader s on s.reader = t.reader
            where idtag_tracker in (
                select max(idtag_tracker) from tag_tracker group by tag_id desc
            )
            and s.status = 1
            order by s.store;
            """
        )
        return tags

    def store_stock(self):
        query = """
            select count(idtag_tracker) as stock, s.store from tag_tracker t
            inner join store_reader s on s.reader = t.reader
            and s.status = 1 and t.status = 1
            group by s.store
            order by stock desc;
            """
        return execute_raw_query(query, None, 'store_stock')

    def tag_flow(self, start_date, end_date):
        query = """
            select s.store, a.in_flow, b.out_flow from
            (select reader, flow as in_flow from
            (select reader, count(idtag_tracker) as flow from tag_tracker
            where updated_time between %(start_date)s and %(end_date)s
            and status = 1
            group by reader
            ) c) a
            inner join
            (select reader, flow as out_flow from
            (select reader, count(idtag_tracker) as flow from tag_tracker
            where updated_time between %(start_date)s and %(end_date)s
            and status = 0
            group by reader
            ) d) b on a.reader = b.reader
            inner join store_reader s on s.reader = a.reader;
            """
        params = {'start_date': start_date, 'end_date': end_date}
        return execute_raw_query(query, params, 'tag_flow')


class TagTracker(models.Model):
    class Meta:
        db_table = "tag_tracker"
        managed = False
    idtag_tracker = models.IntegerField(primary_key=True)
    tag_id = models.CharField(max_length=1024, null=False)
    antenna = models.CharField(max_length=1024, null=False)
    reader = models.CharField(max_length=1024, null=False)
    status = models.IntegerField(null=False)
    created_time = models.DateTimeField(null=False)
    updated_time = models.DateTimeField(null=False)
    objects = TagTrackerManager()

    def __str__(self):
        return str(self.__dict__)
