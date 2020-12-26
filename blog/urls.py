from django.contrib import admin
from django.urls import path
from .views import Galery

urlpatterns = [
    path('', Galery.as_view(), name='galery'),
    
]