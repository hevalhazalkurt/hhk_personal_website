from django.urls import path
from .views import ProjectPostListView, ProjectDetailView, ProjectCategoryListView
from . import views


urlpatterns = [
    path("", ProjectPostListView.as_view(), name="project-home"),
    path("<slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path("category/<slug>/", ProjectCategoryListView.as_view(), name="project-category"),
]
