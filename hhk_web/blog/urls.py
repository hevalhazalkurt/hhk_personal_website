from django.urls import path
from .views import BlogPostListView, BlogDetailView
from . import views


urlpatterns = [
    path("", BlogPostListView.as_view(), name="blog-home"),
    path("<slug>/", BlogDetailView.as_view(), name="blog-detail"),
]
