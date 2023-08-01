from django.urls import path, include

urlpatterns = [
    path('', include('limupa.blog.urls')),
    path('', include('limupa.shop.urls')),
    path('', include('limupa.user.urls')),

]
