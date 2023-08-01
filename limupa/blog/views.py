from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post


class BlogLeft(ListView):
    model = Post
    template_name = 'blog-left-sidebar.html'
    context_object_name = 'posts'


class BlogLeftDetails(DetailView):
    model = Post
    template_name = 'blog-details-right-sidebar.html'
    context_object_name = 'detailpost'

    def get_queryset(self):
        data = super().get_queryset()
        data['recent_posts'] = Post.objects.all().order_by('-created_at')[:10]
        return data
class BlogList(TemplateView):
    template_name = 'blog-list.html'


class Index(TemplateView):
    template_name = 'index.html'
