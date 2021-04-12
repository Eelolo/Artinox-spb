from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *
# Create your views here.

menu = ['Главная','Каталог','Портфолио','Статьи',]

def index(request):
    # posts =
    return render(request, "artinox_spb/index.html", {'title':'Artinox Металлоконструкции', 'menu':menu})

def about(request):
    return render(request, "artinox_spb/about.html", {'title':'О компании Artinox'})

