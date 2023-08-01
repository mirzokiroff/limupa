from django.urls import path
from blog.views import ShoppingCart, W404, AboutUs, Index, Index2, Index3, Index4, WishList, Blog2Col, Blog3Col, \
    BlogAudio, BlogDetails, BlogDetailsLeft, BlogDetailsRight, BlogGallery, BlogLeft, BlogList, BlogListLeft, \
    BlogListRight, BlogVideo, Cart, CheckOut, Compare, Contact, Faq, LoginRegister, ProductDetails, Shop3, Shop4, \
    ShopLeft, ShopRight, ShopList, ShopListLeft, ShopListRight, SingleProduct, SingleProductAffiliate, \
    SingleProductCarousel, SingleProductGalleryLeft, SingleProductGalleryRight, SingleProductGroup, SingleProductNormal, \
    SingleProductSale, SingleProductTabStyleLeft, SingleProductTabStyleRight, SingleProductTabStyleTop

urlpatterns = [
    path('blog/blog-details/', BlogDetailsRight.as_view(), name='blog-details-right'),
    path('', BlogLeft.as_view(), name='blog-left'),

]
