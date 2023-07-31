from django.urls import path
from limupa.user.views import Index, Index2, Index3, Index4, Wishlist

urlpatterns = [
    path('user/', Index.as_view(), name='index'),
    path('user/index2', Index2.as_view(), name='index2'),
    path('user/index3', Index3.as_view(), name='index3'),
    path('user/index4', Index4.as_view(), name='index4'),
    path('user/wishlist', Wishlist.as_view(), name='wishlist'),
]
