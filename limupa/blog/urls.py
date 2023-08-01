from django.urls import path
from blog.views import ShoppingCart, W404, AboutUs, Index, Index2, Index3, Index4, WishList, Blog2Col, Blog3Col, \
    BlogAudio, BlogDetails, BlogDetailsLeft, BlogDetailsRight, BlogGallery, BlogLeft, BlogList, BlogListLeft, \
    BlogListRight, BlogVideo, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, ProductDetails, Shop3, Shop4, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, ShopListRight, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGalleryRight, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleLeft, SingleProductTabStyleRight, SingleProductTabStyleTop

urlpatterns = [
    path('blog/404/', W404.as_view(), name='404'),
    path('blog/about-us/', AboutUs.as_view(), name='about-us'),
    path('blog/blog-2-col/', Blog2Col.as_view(), name='blog-2-col'),
    path('blog/blog-3-col/', Blog3Col.as_view(), name='blog-3-col'),
    path('blog/blog-audio/', BlogAudio.as_view(), name='blog-audio'),
    path('blog/blog-details/', BlogDetails.as_view(), name='blog-details'),
    path('blog/blog-details-left/', BlogDetailsLeft.as_view(), name='blog-details-left'),
    path('blog/blog-details-right/', BlogDetailsRight.as_view(), name='blog-details-right'),
    path('blog/blog-gallery/', BlogGallery.as_view(), name='blog-gallery'),
    path('blog/blog-left/', BlogLeft.as_view(), name='blog-left'),
    path('blog/blog-right/', BlogGallery.as_view(), name='blog-right'),
    path('blog/blog-list/', BlogList.as_view(), name='blog-list'),
    path('blog/blog-list-left/', BlogListLeft.as_view(), name='blog-list-left'),
    path('blog/blog-list-right/', BlogListRight.as_view(), name='blog-list-right'),
    path('blog/blog-video/', BlogVideo.as_view(), name='blog-video'),
    path('blog/cart/', Cart.as_view(), name='cart'),
    path('blog/check-out/', CheckOut.as_view(), name='check-out'),
    path('blog/compare/', Compare.as_view(), name='compare'),
    path('blog/contact/', Contact.as_view(), name='contact'),
    path('blog/faq/', Faq.as_view(), name='faq'),
    path('', Index.as_view(), name='index'),
    path('blog/index2/', Index2.as_view(), name='index2'),
    path('blog/index3/', Index3.as_view(), name='index3'),
    path('blog/index4/', Index4.as_view(), name='index4'),
    path('blog/login-register/', LoginRegister.as_view(), name='login-register'),
    path('blog/product-details/', ProductDetails.as_view(), name='product-details'),
    path('blog/shop-3/', Shop3.as_view(), name='shop-3'),
    path('blog/shop-4/', Shop4.as_view(), name='shop-4'),
    path('blog/shop-left/', ShopLeft.as_view(), name='shop-left'),
    path('blog/shop-right/', ShopRight.as_view(), name='shop-right'),
    path('blog/shop-list/', ShopList.as_view(), name='shop-list'),
    path('blog/shop-list-left/', ShopListLeft.as_view(), name='shop-list-left'),
    path('blog/shop-list-right/', ShopListRight.as_view(), name='shop-list-right'),
    path('blog/shopping-cart/', ShoppingCart.as_view(), name='shopping-cart'),
    path('blog/single-product/', SingleProduct.as_view(), name='single-product'),
    path('blog/single-product-affiliate/', SingleProductAffiliate.as_view(), name='single-product-affiliate'),
    path('blog/single-product-carousel/', SingleProductCarousel.as_view(), name='single-product-carousel'),
    path('blog/single-product-gallery-left/', SingleProductGalleryLeft.as_view(), name='single-product-gallery-left'),
    path('blog/single-product-gallery-right/', SingleProductGalleryRight.as_view(), name='single-product-gallery-right'),
    path('blog/single-product-group/', SingleProductGroup.as_view(), name='single-product-group'),
    path('blog/single-product-normal/', SingleProductNormal.as_view(), name='single-product-normal'),
    path('blog/single-product-sale/', SingleProductSale.as_view(), name='single-product-sale'),
    path('blog/single-product-tab-style-left/', SingleProductTabStyleLeft.as_view(), name='single-product-tab-style-left'),
    path('blog/single-product-tab-style-right/', SingleProductTabStyleRight.as_view(), name='single-product-tab-style-right'),
    path('blog/single-product-tab-style-top/', SingleProductTabStyleTop.as_view(), name='single-product-tab-style-top'),
    path('blog/wish-list/', WishList.as_view(), name='wish-list'),

]
