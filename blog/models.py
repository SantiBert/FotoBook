from django.db import models
from django.conf import settings
from django.utils import timezone

def get_upload_blog_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "blog", str(instance.blog.id), filename])

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

class BlogEntry(models.Model):
    category = models.ForeignKey(Category, verbose_name='category',on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(null=True, blank=True, upload_to='BlogEntry/')
    active = models.BooleanField(default=True)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    images = models.ImageField(null=True, blank=True, upload_to='Images/')
    gallery = models.ManyToManyField(BlogEntry)
    