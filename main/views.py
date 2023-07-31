from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


def NotfoundView(request):
    return render(request, '404.html')
