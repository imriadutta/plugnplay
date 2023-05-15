from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=500)
    content = models.FileField()
    description = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
