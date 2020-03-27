from django.contrib import admin
from .models import ProjectPost, ProjectCategory


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProjectPost, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
