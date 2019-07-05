from django.shortcuts import redirect


def redirect_cinemas(request):
    return redirect('index_url', permanent=True)
