from django.shortcuts import render

def Home(request):

    return render(request, "landing.html")

def AboutUs(request):

    return render(request, "about-us.html")

def Contact(request):

    return render(request, "contact-us.html")