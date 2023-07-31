from django.urls import path, include

urlpatterns = [
    path('post/', include('limupa.blog.urls')),
    path('', include('limupa.shop.urls')),
    path('users/', include('limupa.user.urls')),

]
