
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("projects/", include("project.urls")),
    path("about/", blog_views.about, name="about"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
