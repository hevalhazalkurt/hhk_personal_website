from django.urls import path
from .views import ProjectPostListView, ProjectDetailView
from . import views


urlpatterns = [
    path("", ProjectPostListView.as_view(), name="project-home"),
    path("<slug>/", ProjectDetailView.as_view(), name="project-detail"),
]
