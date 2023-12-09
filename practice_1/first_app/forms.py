from django import forms
from django.forms.widgets import NumberInput
import datetime

class ExampleForm(forms.Form):
    name = forms.CharField(max_length = 10 )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}) )
    email = forms.EmailField(label="Please enter your email address")
    agree = forms.BooleanField()
    date = forms.DateField(required = False, initial=datetime.date.today)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1999', '2000', '2003']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    Decimal_value = forms.DecimalField(initial=10)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    