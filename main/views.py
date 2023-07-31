from django.shortcuts import render
# from main.models import author, about_me, my_tools


def index(request):
    return render(request, 'index.html')
