from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', include('users.urls')),
    path('', include('frontend.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

