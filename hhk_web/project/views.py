from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProjectPost


dummy_projects = [
      {
          "client": "Company A",
          "title": "Project 1",
          "position": "Jr. Python Developer",
          "category": "Development",
          "content": "First project content",
          "date_posted": "March 2, 2019",
      },
      {
          "client": "Company B",
          "title": "Project 2",
          "position": "Director",
          "category": "Filmmaking",
          "content": "Second project content",
          "date_posted": "March 5, 2019",
      },
      {
          "client": "Company C",
          "title": "Project 3",
          "position": "Producer",
          "category": "Filmmaking",
          "content": "Third project content",
          "date_posted": "March 7, 2019",
      },
]


def projecthome(request):
    #context = {"project_posts": dummy_projects}
    context = {"project_posts": ProjectPost.objects.all()}
    return render(request, "project/projecthome.html", context)


class ProjectPostListView(ListView):
    model = ProjectPost
    template_name = "project/projecthome.html"
    context_object_name = "project_posts"
    ordering = ["-date_posted"]
    paginate_by = 10



class ProjectDetailView(DetailView):
    model = ProjectPost
    template_name = "project/project_detail.html"
