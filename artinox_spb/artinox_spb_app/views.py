from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.middleware.csrf import get_token
from django.views.generic import ListView, DetailView



from .forms import *
from .models import *
# Create your views here.

menu = [{'title': 'главная', 'url': 'main'},
        {'title': 'портфолио', 'url': 'portfolio'},
        {'title': 'о нас', 'url': 'about'},
        {'title': 'контакты', 'url': 'contacts'},
        {'title': 'документы', 'url': 'documents'},
        ]


class ArtinoxMain(ListView):
    model = PageContent
    template_name = 'artinox_spb/index.html'
    # context_object_name =


def index(request):
    posts = PageContent.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, "artinox_spb/index.html", context=context,)

def upload_files(request):
    posts = PageContent.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    return redirect('main')
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