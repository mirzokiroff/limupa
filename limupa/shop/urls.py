from django.urls import path
from shop.views import ShoppingCart, WishList, Cart, CheckOut, Compare, Contact, Faq, \
    ProductDetails, ShopLeft, SingleProductNormal, Index

# from shop.views import setcookie

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', CheckOut.as_view(), name='check-out'),
    path('compare/', Compare.as_view(), name='compare'),
    path('product-details/', ProductDetails.as_view(), name='product-details'),
    path('', ShopLeft.as_view(), name='shop'),
    path('hopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('single-product/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('wishlist/', WishList.as_view(), name='wishlist'),
    # path('setcookie', setcookie, name='cookie'),
    path('', Index.as_view(), name='index'),
]
