from django.shortcuts import render


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
    context = {"blog_posts": dummy_posts}
    return render(request, "blog/bloghome.html", context)
