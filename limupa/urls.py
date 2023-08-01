from django.urls import path, include

from shop.views import Index, W404

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('users/', include('user.urls')),
    path('', Index.as_view(), name='index'),
    path('404/', W404.as_view(), name='404'),
]
