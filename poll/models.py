from datetime import datetime
from django.db import models


class Video(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    publishing_datetime = models.DateTimeField(default=datetime.now)
    thumbnail_URL = models.URLField(blank=True)
    channel_id = models.CharField(max_length=200, null=True, blank=True)
    channel_title = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('-publishing_datetime',)
        db_table = 'video'
        indexes = [
            models.Index(fields=["title", "description"]),
        ]
