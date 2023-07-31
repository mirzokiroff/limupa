from django.urls import path, include

urlpatterns = [
    path('', include('limupa.blog.urls')),
    path('users', include('limupa.user.urls')),
    path('shop', include('limupa.shop.urls')),
]
