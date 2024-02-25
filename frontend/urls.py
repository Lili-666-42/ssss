from django.urls import path
from . import views

urlpatterns = [
    path('art/<int:art_id>', views.art, name='art'),
    path('user', views.user, name='user'),
    path('show/<int:user_id>', views.show, name='show'),
    path('home/', views.contact, name='home'),
    path('home2/', views.contact2, name='home2'),
]


