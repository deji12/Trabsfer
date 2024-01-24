from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='blog'),
    path('post-detail/<slug:slug>/', views.PostDetail, name='post-detail'),
]