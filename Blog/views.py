from django.shortcuts import render
from .models import *

def Home(request):

    return render(request, "blog-grid.html")