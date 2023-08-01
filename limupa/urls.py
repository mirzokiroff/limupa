from django.urls import path, include

from shop.views import Index

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('', include('shop.urls')),
    path('users/', include('user.urls')),
    path('', Index.as_view(), name='index')
]
