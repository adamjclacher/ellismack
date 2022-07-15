from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")

def contactPage(request):
    return render(request, "contact.html")

def whoWeAre(request):
    return render(request, "whoWeAre.html")

def whoWeWorkWith(request):
    return render(request, "whoWeWorkWith.html")
