from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('home', index),
    path('main', index),
    path('about', about),
]