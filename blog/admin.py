from django.contrib import admin
from .models import Category, BlogEntry, Images

admin.site.register(Category)
admin.site.register(BlogEntry)
admin.site.register(Images)