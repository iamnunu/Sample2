from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    imglink=models.CharField(max_length=200,default="null")
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=400)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)
    published_upto=models.DateTimeField(
           default=timezone.now)
    code=models.CharField(max_length=50,default="null")
    category=models.CharField(max_length=50,default="null")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title