from django.urls import path
from user.views import ShoppingCart, Index, WishList, LoginRegister, ProductDetails, Shop3, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleTop, \
    UserLoginView, AboutUs

urlpatterns = [
    path('aboutus/', AboutUs.as_view(), name='aboutus'),
    path('login-register/', LoginRegister.as_view(), name='login-register'),
    path('login-register/', UserLoginView.as_view(), name='login'),
    path('product-details/', ProductDetails.as_view(), name='product-details'),
    path('shop-3/', Shop3.as_view(), name='shop-3'),
    path('shop-left/', ShopLeft.as_view(), name='shop-left'),
    path('shop-right/', ShopRight.as_view(), name='shop-right'),
    path('shop-list/', ShopList.as_view(), name='shop-list'),
    path('shop-list-left/', ShopListLeft.as_view(), name='shop-list-left'),
    path('shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('single-product/', SingleProduct.as_view(), name='single-product'),
    path('single-product-affiliate/', SingleProductAffiliate.as_view(), name='single-product-affiliate'),
    path('single-product-carousel/', SingleProductCarousel.as_view(), name='single-product-carousel'),
    path('single-product-gallery-left/', SingleProductGalleryLeft.as_view(), name='single-product-gallery-left'),
    path('single-product-group/', SingleProductGroup.as_view(), name='single-product-group'),
    path('single-product-normal/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('single-product-sale/', SingleProductSale.as_view(), name='single-product-sale'),
    path('single-product-tab-style-top/', SingleProductTabStyleTop.as_view(), name='single-product-tab-style-top'),
    # path('user/wishlist/', WishList.as_view(), name='wishlist'),
]
