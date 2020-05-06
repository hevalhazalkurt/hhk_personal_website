from django.urls import path
from .views import BlogPostListView, BlogDetailView , BlogCategoryListView, HomePageView
from . import views


urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("blog/", BlogPostListView.as_view(), name="blog-home"),
    path("blog/<slug>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blog/category/<slug>/", BlogCategoryListView.as_view(), name="blog-category"),
]
