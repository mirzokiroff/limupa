from django.urls import path
from main.views import home
# from main.views import HomeView

urlpatterns = [
    path('', home, name='index'),
    # path('', HomeView.as_view(), name='index'),
    # path('404', notfound, name='404'),
]
