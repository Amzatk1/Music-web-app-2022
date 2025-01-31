from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_album_viewer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('app_pages.urls')),
    path('albums/', include('app_album_viewer.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
