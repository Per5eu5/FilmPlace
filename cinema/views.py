from django.shortcuts import render
from django.views import View
from .forms import *
from django.contrib.auth.models import User


class IndexCinema(View):
    def get(self, request):
        form = AddPlaceForm()
        return render(request, 'cinema/add_place.html', {'form': form})

    def post(self, request):
        form = AddPlaceForm()
        bound_form = AddPlaceForm(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False) #Сохраняем промежуточное состояние в памяти

            if request.user.id is not None:
                new_obj.user = request.user
            else:
                new_obj.user = User.objects.get(id=4) #Анонимный юзер

            new_obj.save()
            return render(request, 'cinema/add_place.html', {'form': form})

        return render(request, 'cinema/add_place.html', {'form': form})
