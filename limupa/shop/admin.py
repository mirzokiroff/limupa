from django.contrib import admin
from .models import GeneralProductCategory, ProductCategory

admin.site.register((GeneralProductCategory, ProductCategory))
