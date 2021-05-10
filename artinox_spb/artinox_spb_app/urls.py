from django.urls import path

from .views import *

urlpatterns = [
    path('', ArtinoxMain.as_view(), name='main'),
    path('main', ArtinoxMain.as_view(), name='main'),
    path('portfolio', portfolio, name='portfolio'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('documents', documents, name='documents'),
    path('upload_files', upload_files, name='upload_files')
]