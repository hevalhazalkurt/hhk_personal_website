from django.contrib import admin
from .models import BlogPost, BlogCategory


admin.site.register(BlogPost)
admin.site.register(BlogCategory)
