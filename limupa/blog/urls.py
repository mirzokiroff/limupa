from django.urls import path
from limupa.blog.views import Index, Index2, Index3, Index4, WishList, ShoppingCart

urlpatterns = [
    path('blog/', Index.as_view(), name='index'),
    path('blog/index2/', Index2.as_view(), name='index2'),
    path('blog/index3/', Index3.as_view(), name='index3'),
    path('blog/index4/', Index4.as_view(), name='index4'),
    path('blog/wish-list/', WishList.as_view(), name='wishlist'),
    path('blog/shopping-cart/', ShoppingCart.as_view(), name='shoppingcart'),
]
