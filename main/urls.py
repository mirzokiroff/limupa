from django.urls import path
from main.views import Index
# from main.views import HomeView

urlpatterns = [
    path('', Index.as_view, name='index'),
    # path('', HomeView.as_view(), name='index'),
    # path('404', notfound, name='404'),
]
