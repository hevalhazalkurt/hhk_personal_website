from django.db import models
from django.utils import timezone

class ProjectPost(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    link = models.URLField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=250)
    content = models.TextField()
    category = models.CharField(max_length=250)


    def __str__(self):
        return self.title
