from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about-us', views.AboutUs, name='about-us'),
    path('contact-us', views.Contact, name='contact-us'),
]