from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import ProjectPost, ProjectCategory



class ProjectPostListView(ListView):
    model = ProjectPost
    template_name = "project/projecthome.html"
    context_object_name = "project_posts"
    ordering = ["-date_posted"]



class ProjectDetailView(DetailView):
    model = ProjectPost
    template_name = "project/project_detail.html"




class ProjectCategoryListView(ListView):
    model = ProjectPost
    template_name = "project/category_projects.html"
    context_object_name = "category_projects"


    def get_queryset(self):
        category = get_object_or_404(ProjectCategory, slug=self.kwargs.get("slug"))
        return ProjectPost.objects.filter(category_id=category).order_by("-date_posted")
