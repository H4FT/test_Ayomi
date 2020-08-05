from django.shortcuts import render
from django.http import HttpResponse
from .models import Identif
from .form import identif_mail, identif_name

# Create your views here.

def index(request):
    form_mail = email(request)
    form_name = name(request)
    return render(request, 'accueil/form.html', {'form_mail': form_mail, 'form_name': form_name})


def email(request):
    if request.method == 'POST':
        Identif.email = identif_mail(request.POST)
        Identif.save(update_fields['email'])
        if form.is_valid():
            return HttpResponse('/thanks/')
    else:
        form = identif_mail()

    return (form)

def name(request):
    if request.method == 'POST':
        Identif.name = identif_name(request.POST)
        Identif.save(update_fields['name'])
        if form.is_valid():
            return HttpResponse('/thanks/')
    else:
        form = identif_name()

    return (form)

