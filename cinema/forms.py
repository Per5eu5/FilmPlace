from django import forms
from .models import Place


class AddPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'hall', 'row', 'seat', 'armrests', 'comment']

        labels = {
            'name': 'Название кинотеатра',
            'hall': 'Зал',
            'row': 'Ряд',
            'seat': 'Место',
            'armrests': 'Откидываются ли подлокотники?',
            'comment': 'Впечатление от места',
        }
