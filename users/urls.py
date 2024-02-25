from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'),
    path('out/', views.logout_user , name='out'),
    path('login/', views.login_view, name='login'),
]
