from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index_url'),
    path('movie/', MovieList.as_view(), name='movie_list')
]
