from django.urls import path
from limupa.user.views import ShoppingCart, W404, AboutUs, Index, Index2, Index3, Index4, WishList, Blog2Col, Blog3Col, \
    BlogAudio, BlogDetails, BlogDetailsLeft, BlogDetailsRight, BlogGallery, BlogLeft, BlogList, BlogListLeft, \
    BlogListRight, BlogVideo, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, ProductDetails, Shop3, Shop4, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, ShopListRight, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGalleryRight, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleLeft, SingleProductTabStyleRight, SingleProductTabStyleTop

urlpatterns = [
    path('user/404/', W404.as_view(), name='404'),
    path('user/about-us/', AboutUs.as_view(), name='about-us'),
    path('user/blog-2-col/', Blog2Col.as_view(), name='blog-2-col'),
    path('user/blog-3-col/', Blog3Col.as_view(), name='blog-3-col'),
    path('user/blog-audio/', BlogAudio.as_view(), name='blog-audio'),
    path('user/blog-details/', BlogDetails.as_view(), name='blog-details'),
    path('user/blog-details-left/', BlogDetailsLeft.as_view(), name='blog-details-left'),
    path('user/blog-details-right/', BlogDetailsRight.as_view(), name='blog-details-right'),
    path('user/blog-gallery/', BlogGallery.as_view(), name='blog-gallery'),
    path('user/blog-left/', BlogLeft.as_view(), name='blog-left'),
    path('user/blog-right/', BlogGallery.as_view(), name='blog-right'),
    path('user/blog-list/', BlogList.as_view(), name='blog-list'),
    path('user/blog-list-left/', BlogListLeft.as_view(), name='blog-list-left'),
    path('user/blog-list-right/', BlogListRight.as_view(), name='blog-list-right'),
    path('user/blog-video/', BlogVideo.as_view(), name='blog-video'),
    path('user/cart/', Cart.as_view(), name='cart'),
    path('user/check-out/', CheckOut.as_view(), name='check-out'),
    path('user/compare/', Compare.as_view(), name='compare'),
    path('user/contact/', Contact.as_view(), name='contact'),
    path('user/faq/', Faq.as_view(), name='faq'),
    path('', Index.as_view(), name='index'),
    path('user/index2/', Index2.as_view(), name='index2'),
    path('user/index3/', Index3.as_view(), name='index3'),
    path('user/index4/', Index4.as_view(), name='index4'),
    path('user/login-register/', LoginRegister.as_view(), name='login-register'),
    path('user/product-details/', ProductDetails.as_view(), name='product-details'),
    path('user/shop-3/', Shop3.as_view(), name='shop-3'),
    path('user/shop-4/', Shop4.as_view(), name='shop-4'),
    path('user/shop-left/', ShopLeft.as_view(), name='shop-left'),
    path('user/shop-right/', ShopRight.as_view(), name='shop-right'),
    path('user/shop-list/', ShopList.as_view(), name='shop-list'),
    path('user/shop-list-left/', ShopListLeft.as_view(), name='shop-list-left'),
    path('user/shop-list-right/', ShopListRight.as_view(), name='shop-list-right'),
    path('user/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('user/single-product/', SingleProduct.as_view(), name='single-product'),
    path('user/single-product-affiliate/', SingleProductAffiliate.as_view(), name='single-product-affiliate'),
    path('user/single-product-carousel/', SingleProductCarousel.as_view(), name='single-product-carousel'),
    path('user/single-product-gallery-left/', SingleProductGalleryLeft.as_view(), name='single-product-gallery-left'),
    path('user/single-product-gallery-right/', SingleProductGalleryRight.as_view(), name='single-product-gallery-right'),
    path('user/single-product-group/', SingleProductGroup.as_view(), name='single-product-group'),
    path('user/single-product-normal/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('user/single-product-sale/', SingleProductSale.as_view(), name='single-product-sale'),
    path('user/single-product-tab-style-left/', SingleProductTabStyleLeft.as_view(), name='single-product-tab-style-left'),
    path('user/single-product-tab-style-right/', SingleProductTabStyleRight.as_view(), name='single-product-tab-style-right'),
    path('user/single-product-tab-style-top/', SingleProductTabStyleTop.as_view(), name='single-product-tab-style-top'),
    path('user/wish-list/', WishList.as_view(), name='wish-list'),

]
