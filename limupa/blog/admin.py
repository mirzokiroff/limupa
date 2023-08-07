from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Post, Comment, BlogCategory

# Register your models here.
admin.site.register((Comment, BlogCategory))


@admin.register(Post)
class AdminPost(ImportExportModelAdmin):
    pass
