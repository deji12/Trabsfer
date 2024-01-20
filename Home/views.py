from django.shortcuts import render
from Globals.models import Rate

def Home(request):

    naira = Rate.objects.get(currency_name='Nigerian naira')
    rouble = Rate.objects.get(currency_name='Russian rouble')

    context = {
        "naira": naira.rate,
        "rouble": rouble.rate,
    }

    return render(request, "landing.html", context)

def AboutUs(request):

    return render(request, "about-us.html")

def Contact(request):

    return render(request, "contact-us.html")