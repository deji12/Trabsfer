from django.shortcuts import render

def NotFound(request, exception=None):

    return render(request, "404.html", status=404)
