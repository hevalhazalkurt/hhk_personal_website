from django.shortcuts import render
from .models import BlogPost

dummy_posts = [
      {
          "author": "Heval Hazal Kurt",
          "title": "Blog Post 1",
          "category": "Development",
          "content": "First post content",
          "date_posted": "August 27, 2018",
      },
      {
          "author": "Heval Hazal Kurt",
          "title": "Blog Post 2",
          "category": "Filmmaking",
          "content": "Second post content",
          "date_posted": "August 29, 2018",
      },
      {
          "author": "Heval Hazal Kurt",
          "title": "Blog Post 3",
          "category": "Life",
          "content": "Third post content",
          "date_posted": "September 2, 2018",
      },
]


def bloghome(request):
    #context = {"blog_posts": dummy_posts}
    context = {"blog_posts": BlogPost.objects.all()}
    return render(request, "blog/bloghome.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def contact(request):
    return render(request, "blog/contact.html", {"title": "Contact"})


def home(request):
    return render(request, "blog/home.html")
