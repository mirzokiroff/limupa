from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post, BlogCategory


class BlogLeft(ListView):
    model = Post
    template_name = 'blog-left-sidebar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['posts'] = Post.objects.all()
        data['recent'] = Post.objects.all().order_by('-created_at')[:10]
        data['category'] = BlogCategory.objects.all()
        return data


class BlogLeftDetails(DetailView):
    model = Post
    template_name = 'blog-details-right-sidebar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['detailpost'] = Post.objects.filter(id=self.object).first()
        data['postcategory'] = Post.objects.all().post_category
        data['category'] = BlogCategory.objects.all()
        return data


class BlogList(TemplateView):
    template_name = 'blog-list.html'


class Index(TemplateView):
    template_name = 'index.html'
