from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class Index2(TemplateView):
    template_name = 'index-2.html'


class Index3(TemplateView):
    template_name = 'index-3.html'


class Index4(TemplateView):
    template_name = 'index-4.html'

