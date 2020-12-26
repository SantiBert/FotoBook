from django.shortcuts import render
from .models import Category, BlogEntry, Images
from django.views import View

class Galery(View):
    def get(self, request, *args, **kwargs):
        galery = Images.objects.all()
        context = {'galery':galery}
        return render(request, 'gallery.html',context)


