from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField('shop.ProductCategory', related_name='post')
    title = models.CharField(max_length=255)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class BlogImages(models.Model):
    images = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
