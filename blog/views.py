from django.shortcuts import render
from .models import Category, BlogEntry, Images
from django.views import View
from django.views.generic.list import ListView

class Galery(View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        galery = Images.objects.all()
        context = {
            'galery':galery, 
            'category':category,
            }
        return render(request, 'gallery.html',context)

class BlogEntryView(ListView):
    def get(self, request, slug, *args, **kwargs):
        post = BlogEntry.objects.filter(active=True)
        category = Category.objects.get(slug)
        categories = Category.objects.filter(active=True)
        context = {
            'post':post,
            'category':category,
            'categories':categories,
        }
        return render(request, 'blog.html',context)


