
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("projects/", include("project.urls")),
    path("about/", blog_views.about, name="about"),
    path("contact/", blog_views.contact, name="contact"),
    path("", blog_views.home, name="home"),
]
