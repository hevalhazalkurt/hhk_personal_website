from django.urls import path
from .views import ProjectPostListView, ProjectDetailView
from . import views


urlpatterns = [
    path("", ProjectPostListView.as_view(), name="project-home"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]
