from django.shortcuts import render


def index(request):
    return render(request, 'defaultpages/index.html')

def about(request):
    return render(request, 'defaultpages/about.html')