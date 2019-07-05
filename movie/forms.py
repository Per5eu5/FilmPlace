from django import forms
from .models import Solovey
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    title = forms.CharField(max_length=50, label="Название фильма", required=False)
    theatre = forms.CharField(max_length=50, label="Кинотеатр", required=False)
    cost = forms.CharField(max_length=10, label="Цена", required=False)

# class SearchForm(forms.ModelForm):
#
#     class Meta:
#         model = Solovey
#         fields = ['title']
#
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#         }