from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:username>/<int:code>/', views.ResetPassword, name='reset-password'),
]