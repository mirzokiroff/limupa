from django.urls import path, include

urlpatterns = [
    path('post/', include('blog.urls')),
    path('', include('shop.urls')),
    path('users/', include('user.urls')),

]
