from django.urls import path
from limupa.shop.views import Index, Index2, Index3, Index4, Wishlist

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('shop/index2', Index2.as_view(), name='index2'),
    path('shop/index3', Index3.as_view(), name='index3'),
    path('shop/index4', Index4.as_view(), name='index4'),
    path('shop/wishlist', Wishlist.as_view(), name='wishlist'),
]
