from django.shortcuts import redirect
from django.shortcuts import render


def index(request):
    return render(request, './movie/index.html')


def redirect_cinemas(request):
    return redirect('index_url', permanent=True)
