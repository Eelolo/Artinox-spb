from django.urls import path

from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('main', MainView.as_view(), name='main'),
    path('portfolio', portfolio, name='portfolio'),
    path('about', AboutView.as_view(), name='about'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('documents', documents, name='documents'),
    path('upload_files', UploadFiles.upload_files, name='upload_files')
]