from django.urls import path
from . import views

urlpatterns = [
    path("", views.projecthome, name="project-home"), 
]
