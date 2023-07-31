from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('limupa.urls')),
    path('', include('limupa.shop.urls')),
    path('users/', include('limupa.user.urls')),
    path('blog', include('limupa.blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
