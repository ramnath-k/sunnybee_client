from django.contrib import admin

from .models import Crate, StoreReader, TagTracker, WaitTime

admin.site.register(Crate)
admin.site.register(StoreReader)
admin.site.register(TagTracker)
admin.site.register(WaitTime)

