from django.urls import path
from limupa.user.views import Index

urlpatterns = [
    path('user/', Index.as_view(), name='index')
]
