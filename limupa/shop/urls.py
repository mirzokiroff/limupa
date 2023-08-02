from django.urls import path
from limupa.shop.views import ShoppingCart, WishList, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, \
    ProductDetails, ShopLeft, SingleProductNormal
# from shop.views import setcookie

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', CheckOut.as_view(), name='check-out'),
    path('compare/', Compare.as_view(), name='compare'),
    path('contact/', Contact.as_view(), name='contact'),
    path('faq/', Faq.as_view(), name='faq'),
    path('login-register/', LoginRegister.as_view(), name='login-register'),
    path('product-details/', ProductDetails.as_view(), name='product-details'),
    path('shop', ShopLeft.as_view(), name='shop-left'),
    path('shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('single-product/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('wish-list/', WishList.as_view(), name='wish-list'),
    # path('setcookie', setcookie, name='cookie'),
]
