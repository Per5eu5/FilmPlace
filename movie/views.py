from django.shortcuts import render
from .models import Solovey

from django.views.generic import View
from .forms import SearchForm
from django.db.models import Q


class MovieList(View):
    def get(self, request):
        movie = Solovey.objects.all()[:5]
        form = SearchForm()
        return render(request, 'movie/movie_list.html', context={'movie': movie, 'form': form})

    def post(self, request):

        bound_form = SearchForm(request.POST)

        if bound_form.is_valid:
            print(bound_form)
            films = Solovey.objects.filter(Q(title__icontains=request.POST['title']) | Q(cost=request.POST['cost']))
            return render(request, 'movie/movie_list.html', context={'movie': films})
        else:
            return render(request, 'movie/movie_list.html', context={'movie': Solovey.objects.all()})
