from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import ProjectPost, ProjectCategory


class ProjectPostListView(ListView):
    model = ProjectPost
    template_name = "project/projecthome.html"
    context_object_name = "project_posts"
    ordering = ["-date_posted"]
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_categories'] = ProjectCategory.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = ProjectPost
    template_name = "project/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = ProjectPost.objects.filter(category=self.object.category).order_by('?')[:3]
        return context




class ProjectCategoryListView(ListView):
    model = ProjectPost
    template_name = "project/category_projects.html"
    context_object_name = "category_projects"
    paginate_by = 5


    def get_queryset(self):
        category = get_object_or_404(ProjectCategory, slug=self.kwargs.get("slug"))
        return ProjectPost.objects.filter(category_id=category).order_by("-date_posted")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_categories'] = ProjectCategory.objects.all()
        return context
