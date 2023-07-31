from django.urls import path
from limupa.shop.views import Index, Index2, Index3, Index4, WishList, ShoppingCart

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('shop/index2/', Index2.as_view(), name='index2'),
    path('shop/index3/', Index3.as_view(), name='index3'),
    path('shop/index4/', Index4.as_view(), name='index4'),
    path('shop/wish-list/', WishList.as_view(), name='wishlist'),
    path('shop/shopping-cart/', ShoppingCart.as_view(), name='shoppingcart'),
]
