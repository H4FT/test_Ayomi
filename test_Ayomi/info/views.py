from django.shortcuts import render
from accueil.models import Identif
from django.http import HttpResponse
from .form import modal

# Create your views here.

def index(request):
    return render(request, 'info/home.html')