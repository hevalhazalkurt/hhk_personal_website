from django.urls import path
from . import views

urlpatterns = [
    path("", views.bloghome, name="blog-home"),
]
