from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('limupa.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
