from django.urls import path
from blog.views import BlogLeft, BlogLeftDetails, Index

urlpatterns = [
    path('blog-details/<int:pk>/', BlogLeftDetails.as_view(), name='blog-details-right'),
    # path('filter/<str:title>/', )
    path('blog', BlogLeft.as_view(), name='blog-left'),
    path('', Index.as_view(), name='index'),

]
