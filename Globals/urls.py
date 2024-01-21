from django.urls import path
from . import views

urlpatterns = [
    path("not-found/", views.NotFound, name='not-found'),
]