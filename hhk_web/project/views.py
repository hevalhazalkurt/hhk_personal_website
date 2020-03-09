from django.shortcuts import render


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
    context = {"project_posts": dummy_projects}
    return render(request, "project/projecthome.html", context)
