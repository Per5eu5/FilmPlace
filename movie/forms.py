from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=50, label="Название фильма", required=False)
    theatre = forms.CharField(max_length=50, label="Кинотеатр", required=False)
    cost = forms.CharField(max_length=10, label="Цена", required=False)