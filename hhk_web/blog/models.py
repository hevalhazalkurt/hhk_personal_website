from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = "Heval Hazal Kurt"


    def __str__(self):
        return self.title
