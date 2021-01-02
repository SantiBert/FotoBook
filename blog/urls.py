from django.contrib import admin
from django.urls import path
from .views import Galery, BlogEntryListView, DetailedBlogEntry

urlpatterns = [
    path('', Galery.as_view(), name='galery'),
    path('<slug:slug>/', BlogEntryListView.as_view(), name='blogEntry'),
    path('<str:name>/', DetailedBlogEntry.as_view(), name='blogEntry'),
]