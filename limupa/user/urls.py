from django.urls import path
from limupa.user.views import Index, Index2, Index3, Index4, WishList, ShoppingCart

urlpatterns = [
    path('user/', Index.as_view(), name='index'),
    path('user/index2/', Index2.as_view(), name='index2'),
    path('user/index3/', Index3.as_view(), name='index3'),
    path('user/index4/', Index4.as_view(), name='index4'),
    path('user/wish-list/', WishList.as_view(), name='wishlist'),
    path('user/shopping-cart/', ShoppingCart.as_view(), name='shoppingcart'),
]
