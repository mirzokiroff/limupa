from django.urls import path
from shop.views import ShoppingCart, W404, AboutUs, Index, Index2, Index3, Index4, WishList, Blog2Col, Blog3Col, \
    BlogAudio, BlogDetails, BlogDetailsLeft, BlogDetailsRight, BlogGallery, BlogLeft, BlogList, BlogListLeft, \
    BlogListRight, BlogVideo, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, ProductDetails, Shop3, Shop4, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, ShopListRight, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGalleryRight, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleLeft, SingleProductTabStyleRight, SingleProductTabStyleTop

urlpatterns = [
    path('shop/404/', W404.as_view(), name='404'),
    path('shop/about-us/', AboutUs.as_view(), name='about-us'),
    path('shop/blog-3-col/', Blog3Col.as_view(), name='blog-3-col'),
    path('shop/blog-details/', BlogDetailsLeft.as_view(), name='blog-details-left'),
    path('shop/cart/', Cart.as_view(), name='cart'),
    path('shop/check-out/', CheckOut.as_view(), name='check-out'),
    path('shop/compare/', Compare.as_view(), name='compare'),
    path('shop/contact/', Contact.as_view(), name='contact'),
    path('shop/faq/', Faq.as_view(), name='faq'),
    path('shop/login-register/', LoginRegister.as_view(), name='login-register'),
    path('shop/product-details/', ProductDetails.as_view(), name='product-details'),
    path('', ShopLeft.as_view(), name='shop-left'),
    path('shop/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('shop/single-product/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('shop/wish-list/', WishList.as_view(), name='wish-list'),
]
