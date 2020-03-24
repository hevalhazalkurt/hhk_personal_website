from django.db import models
from django.utils import timezone
from django.urls import reverse



class BlogCategory(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'blog category'
        verbose_name_plural = 'blog categories'


    def __str__(self):
        return self.title


class BlogPost(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = "Heval Hazal Kurt"
    slug = models.SlugField(max_length=250, unique=True, blank = True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.slug])
