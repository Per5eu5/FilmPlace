from django import forms


class AddPlaceForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название кинотеатра')
    hall = forms.CharField(max_length=50, label='Зал')
    row = forms.CharField(label='Ряд в билете')
    seat = forms.CharField(label='Место в билете')
    armrests = forms.ChoiceField(label='Откидываются ли подлокотники?', choices=(('1', 'да'), ('2', 'нет')))
    comment = forms.CharField(widget=forms.Textarea, label='Ваши впечатления от места')
