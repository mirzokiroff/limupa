from django.urls import path
from limupa.shop.views import ShoppingCart, W404, AboutUs, Index, Index2, Index3, Index4, WishList, Blog2Col, Blog3Col, \
    BlogAudio, BlogDetails, BlogDetailsLeft, BlogDetailsRight, BlogGallery, BlogLeft, BlogList, BlogListLeft, \
    BlogListRight, BlogVideo, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, ProductDetails, Shop3, Shop4, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, ShopListRight, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGalleryRight, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleLeft, SingleProductTabStyleRight, SingleProductTabStyleTop

urlpatterns = [
    path('shop/404/', W404.as_view(), name='404'),
    path('shop/about-us/', AboutUs.as_view(), name='about-us'),
    path('shop/blog-2-col/', Blog2Col.as_view(), name='blog-2-col'),
    path('shop/blog-3-col/', Blog3Col.as_view(), name='blog-3-col'),
    path('shop/blog-audio/', BlogAudio.as_view(), name='blog-audio'),
    path('shop/blog-details/', BlogDetails.as_view(), name='blog-details'),
    path('shop/blog-details-left/', BlogDetailsLeft.as_view(), name='blog-details-left'),
    path('shop/blog-details-right/', BlogDetailsRight.as_view(), name='blog-details-right'),
    path('shop/blog-gallery/', BlogGallery.as_view(), name='blog-gallery'),
    path('shop/blog-left/', BlogLeft.as_view(), name='blog-left'),
    path('shop/blog-right/', BlogGallery.as_view(), name='blog-right'),
    path('shop/blog-list/', BlogList.as_view(), name='blog-list'),
    path('shop/blog-list-left/', BlogListLeft.as_view(), name='blog-list-left'),
    path('shop/blog-list-right/', BlogListRight.as_view(), name='blog-list-right'),
    path('shop/blog-video/', BlogVideo.as_view(), name='blog-video'),
    path('shop/cart/', Cart.as_view(), name='cart'),
    path('shop/check-out/', CheckOut.as_view(), name='check-out'),
    path('shop/compare/', Compare.as_view(), name='compare'),
    path('shop/contact/', Contact.as_view(), name='contact'),
    path('shop/faq/', Faq.as_view(), name='faq'),
    path('', Index.as_view(), name='index'),
    path('shop/index2/', Index2.as_view(), name='index2'),
    path('shop/index3/', Index3.as_view(), name='index3'),
    path('shop/index4/', Index4.as_view(), name='index4'),
    path('shop/login-register/', LoginRegister.as_view(), name='login-register'),
    path('shop/product-details/', ProductDetails.as_view(), name='product-details'),
    path('shop/shop-3/', Shop3.as_view(), name='shop-3'),
    path('shop/shop-4/', Shop4.as_view(), name='shop-4'),
    path('shop/shop-left/', ShopLeft.as_view(), name='shop-left'),
    path('shop/shop-right/', ShopRight.as_view(), name='shop-right'),
    path('shop/shop-list/', ShopList.as_view(), name='shop-list'),
    path('shop/shop-list-left/', ShopListLeft.as_view(), name='shop-list-left'),
    path('shop/shop-list-right/', ShopListRight.as_view(), name='shop-list-right'),
    path('shop/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('shop/single-product/', SingleProduct.as_view(), name='single-product'),
    path('shop/single-product-affiliate/', SingleProductAffiliate.as_view(), name='single-product-affiliate'),
    path('shop/single-product-carousel/', SingleProductCarousel.as_view(), name='single-product-carousel'),
    path('shop/single-product-gallery-left/', SingleProductGalleryLeft.as_view(), name='single-product-gallery-left'),
    path('shop/single-product-gallery-right/', SingleProductGalleryRight.as_view(), name='single-product-gallery-right'),
    path('shop/single-product-group/', SingleProductGroup.as_view(), name='single-product-group'),
    path('shop/single-product-normal/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('shop/single-product-sale/', SingleProductSale.as_view(), name='single-product-sale'),
    path('shop/single-product-tab-style-left/', SingleProductTabStyleLeft.as_view(), name='single-product-tab-style-left'),
    path('shop/single-product-tab-style-right/', SingleProductTabStyleRight.as_view(), name='single-product-tab-style-right'),
    path('shop/single-product-tab-style-top/', SingleProductTabStyleTop.as_view(), name='single-product-tab-style-top'),
    path('shop/wish-list/', WishList.as_view(), name='wish-list'),

]
