from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from utils.validate import validate_email, authenticate

def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if validate_email(email) != True:
            messages.error(request, "Email already in use")
            return redirect('register')
        
        new_user = User.objects.create_user(
            username = f"{firstname}_{lastname}",
            first_name = firstname,
            last_name = lastname,
            password = password,
            email = email
        )
        new_user.save()
        messages.success(request, "Account created! Login now")
        return redirect('login')
    
    context = {
        "status": True
    }

    return render(request, "signup.html", context)


def Login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
        
    context = {
        "status": True
    }

    return render(request, "login.html", context)

def Logout(request):
    logout(request)
    return redirect('login')