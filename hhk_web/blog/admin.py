from django.contrib import admin
from .models import BlogPost, BlogCategory

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
