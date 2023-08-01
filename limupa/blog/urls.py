from django.urls import path
from blog.views import BlogDetailsRight, BlogLeft

urlpatterns = [
    path('blog/blog-details/', BlogDetailsRight.as_view(), name='blog-details-right'),
    path('', BlogLeft.as_view(), name='blog-left'),
]
