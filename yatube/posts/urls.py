from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/<slug:group>/', views.group_posts),
    path('posts/<int:pk>/', views.posts_details),
]
