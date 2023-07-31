from django.urls import path, include

urlpatterns = [
    path('blog/', include('limupa.blog.urls')),
    path('users/', include('limupa.user.urls')),
    path('', include('limupa.shop.urls')),
]
