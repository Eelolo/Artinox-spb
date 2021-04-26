from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *
# Create your views here.

menu = [{'title': 'главная', 'url': 'main'},
        {'title': 'портфолио', 'url': 'portfolio'},
        {'title': 'о нас', 'url': 'about'},
        {'title': 'контакты', 'url': 'contacts'},
        {'title': 'документы', 'url': 'documents'},
        ]



def index(request):
    posts = PageContent.objects.all()
    
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, "artinox_spb/index.html", context=context)

def about(request):
    posts = PageContent.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, "artinox_spb/about.html", context=context)

def contacts(request):
    posts = PageContent.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, "artinox_spb/contacts.html", context=context)

def documents(request):
    posts = PageContent.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, "artinox_spb/documents.html", context=context)

def portfolio(request):
    posts = PageContent.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, "artinox_spb/portfolio.html", context=context)