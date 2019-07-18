from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexCinema.as_view(), name='index_cinema_url'),
]
