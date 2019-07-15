from django.shortcuts import render
from django.http import HttpResponse


def index_cinema(request):
    return HttpResponse('<img src="http://www1.pictures.zimbio.com/gi/Safe+European+Premiere+Inside+Arrivals+DgoQtTF5XFux.jpg" alt="">')
