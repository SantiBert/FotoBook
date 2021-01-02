import pdb

from django.shortcuts import render
from .models import Category, BlogEntry, Images
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class Galery(View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        galery = Images.objects.all()
        context = {
            'galery':galery, 
            'category':category,
            }
        return render(request, 'gallery.html',context)

class BlogEntryListView(ListView):
    def get(self, gallery, request, slug, *args, **kwargs):
        post = BlogEntry.objects.filter(active=True, category__slug=slug)
        image = Images.objects.filter(active=True, BlogEntry__name=gallery)
        context = {
            'posts':post,            
        }
        return render(request, 'blog.html',context)


class DetailedBlogEntry(DetailView):
    def get(self, gallery,name, request, *args, **kwargs):
        post = BlogEntry.objects.get(name)
        image = Images.objects.filter(active=True, post=gallery)
        context = {
            'image':image,
        }
        return render(request, 'detailed_gallery.html',context)
