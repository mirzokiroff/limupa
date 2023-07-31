from django.contrib import admin
from .models import Post, Comment, BlogImages

# Register your models here.
admin.site.register((Post, Comment, BlogImages))
