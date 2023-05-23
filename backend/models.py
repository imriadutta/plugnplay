from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=500)
    content = models.FileField(upload_to='media/')
    description = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class User(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
