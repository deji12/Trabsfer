from django.shortcuts import render
from Globals.models import Rate, Testimonial, FAQ

def Home(request):

    naira = Rate.objects.get(currency_name='Nigerian naira')
    rouble = Rate.objects.get(currency_name='Russian rouble')
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()

    context = {
        "naira": naira.rate,
        "naira_min": 100*rouble.rate,
        "rouble": rouble.rate,
        "testimonials": testimonials,
        "faqs": faqs
    }

    return render(request, "landing.html", context)

def AboutUs(request):

    testimonials = Testimonial.objects.all()

    context = {
        "testimonials": testimonials,
    }

    return render(request, "about-us.html", context)

def Contact(request):

    return render(request, "contact-us.html")