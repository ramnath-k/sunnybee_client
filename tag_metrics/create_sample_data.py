from tag_metrics.models import Crate, TagTracker

def populate_crate():
    crate_template = 'crate_{:04d}'
    i = 0
    for tag in TagTracker.objects.all():
        tag_id = tag.tag_id
        crate = crate_template.format(i)
        i += 1
        status = 1
        crate_model = Crate.objects.map_tag_id_to_crate(crate, tag_id, status)
        print tag_id, crate, status, crate_model.id

