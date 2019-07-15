from django.urls import path

from .views import *

urlpatterns = [
    path('', index_cinema, name='index_cinema_url'),
]
