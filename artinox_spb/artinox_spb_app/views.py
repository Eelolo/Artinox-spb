from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpRequest
from django.middleware.csrf import get_token
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


from .forms import *
from .models import *
# Create your views here.

class MainView(ListView):
    model = PageContent
    template_name = 'artinox_spb/index.html'
    # context_object_name =


class UploadFiles(ListView):
    posts = PageContent.objects.all()

    def upload_files(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            form = UploadFileForm()
        return redirect('main')

class AboutView(ListView):
    model = PageContent
    template_name = 'artinox_spb/about.html'

class ContactsView(ListView):
    model = PageContent
    template_name = 'artinox_spb/contacts.html'

class DocumentsView(ListView):
    model = PageContent
    template_name = 'artinox_spb/documents.html'

class PortfolioView(ListView):
    model = PageContent
    template_name = 'artinox_spb/portfolio.html'
