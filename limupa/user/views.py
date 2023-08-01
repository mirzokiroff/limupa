from django.views.generic import TemplateView
from limupa.user.forms import ContactForm
from limupa.user.utls import send_message


class W404(TemplateView):
    template_name = '404.html'


class AboutUs(TemplateView):
    template_name = 'about-us.html'


class Blog2Col(TemplateView):
    template_name = 'blog-2-column.html'


class Blog3Col(TemplateView):
    template_name = 'blog-3-column.html'


class BlogAudio(TemplateView):
    template_name = 'blog-audio-format.html'


class BlogDetails(TemplateView):
    template_name = 'blog-details.html'


class BlogDetailsLeft(TemplateView):
    template_name = 'blog-details-left-sidebar.html'


class BlogDetailsRight(TemplateView):
    template_name = 'blog-details-right-sidebar.html'


class BlogGallery(TemplateView):
    template_name = 'blog-gallery-format.html'


class BlogLeft(TemplateView):
    template_name = 'blog-left-sidebar.html'


class BlogRight(TemplateView):
    template_name = 'blog-right-sidebar.html'


class BlogList(TemplateView):
    template_name = 'blog-list.html'


class BlogListLeft(TemplateView):
    template_name = 'blog-list-left-sidebar.html'


class BlogListRight(TemplateView):
    template_name = 'blog-list-right-sidebar.html'


class BlogVideo(TemplateView):
    template_name = 'blog-video-format.html'


class Cart(TemplateView):
    template_name = 'cart.html'


class CheckOut(TemplateView):
    template_name = 'checkout.html'


class Compare(TemplateView):
    template_name = 'compare.html'


class Contact(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = ContactForm(data)
        if form.is_valid():
            data = form.cleaned_data
            m = f'''📥 New mail\n📩 From: {data['email']}\n👱 Name: {data['name']}\n📢 Subject: {data['subject']}\n📄 Message: {data['text']}'''
            l = [1038185913, 5467465403, 5553781606]
            for i in l:
                send_message(i, m)
        return self.get(request, *args, **kwargs)


class Faq(TemplateView):
    template_name = 'faq.html'


class Index(TemplateView):
    template_name = 'index.html'


class Index2(TemplateView):
    template_name = 'index-2.html'


class Index3(TemplateView):
    template_name = 'index-3.html'


class Index4(TemplateView):
    template_name = 'index-4.html'


class LoginRegister(TemplateView):
    template_name = 'login-register.html'


class ProductDetails(TemplateView):
    template_name = 'product-details.html'


class Shop3(TemplateView):
    template_name = 'shop-3-column.html'


class Shop4(TemplateView):
    template_name = 'shop-4-column.html'


class ShopLeft(TemplateView):
    template_name = 'shop-left-sidebar.html'


class ShopRight(TemplateView):
    template_name = 'shop-right-sidebar.html'


class ShopList(TemplateView):
    template_name = 'shop-list.html'


class ShopListLeft(TemplateView):
    template_name = 'shop-list-left-sidebar.html'


class ShopListRight(TemplateView):
    template_name = 'shop-list-right-sidebar.html'


class ShoppingCart(TemplateView):
    template_name = 'shopping-cart.html'


class SingleProduct(TemplateView):
    template_name = 'single-product.html'


class SingleProductAffiliate(TemplateView):
    template_name = 'single-product-affiliate.html'


class SingleProductCarousel(TemplateView):
    template_name = 'single-product-carousel.html'


class SingleProductGalleryLeft(TemplateView):
    template_name = 'single-product-gallery-left.html'


class SingleProductGalleryRight(TemplateView):
    template_name = 'single-product-gallery-right.html'


class SingleProductGroup(TemplateView):
    template_name = 'single-product-group.html'


class SingleProductNormal(TemplateView):
    template_name = 'single-product-normal.html'


class SingleProductSale(TemplateView):
    template_name = 'single-product-sale.html'


class SingleProductTabStyleLeft(TemplateView):
    template_name = 'single-product-tab-style-left.html'


class SingleProductTabStyleRight(TemplateView):
    template_name = 'single-product-tab-style-right.html'


class SingleProductTabStyleTop(TemplateView):
    template_name = 'single-product-tab-style-top.html'


class WishList(TemplateView):
    template_name = 'wishlist.html'














