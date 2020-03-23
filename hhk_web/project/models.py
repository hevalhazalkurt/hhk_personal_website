from django.db import models
from django.utils import timezone


class ProjectCategory(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'project category'
        verbose_name_plural = 'project categories'


    def __str__(self):
        return self.title



class ProjectPost(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    link = models.URLField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
