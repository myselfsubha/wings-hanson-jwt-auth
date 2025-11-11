from django.contrib import admin
from .models import StreamPlatform, WatchList, Review

admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(Review)