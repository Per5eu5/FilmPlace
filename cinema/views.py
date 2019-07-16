from django.shortcuts import render
from .forms import AddPlaceForm


def index_cinema(request):
    form = AddPlaceForm()
    return render(request, 'cinema/add_place.html', {'form': form})
