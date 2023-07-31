from django.db import models


class Core(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GeneralProductCategory(Core):
    created_at = None
    updated_at = None

class ProductCategory(Core):
    created_at = None
    updated_at = None
    general = models.ForeignKey(GeneralProductCategory, on_delete=models.CASCADE)

class Product(Core):
    id = None
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug url')
    description = models.TextField()
    images = None
    info = None
