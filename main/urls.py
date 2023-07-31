from django.urls import path
from main.views import index
from main.views import HomeView

urlpatterns = [
    path('', index, name='index'),
    path('', HomeView.as_view(), name='index'),
    # path('404', notfound, name='404'),
]
