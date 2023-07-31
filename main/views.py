from django.shortcuts import render
# from main.models import author, about_me, my_tools


# Create your views here.
def home(request):
    return render(request, 'index.html')
