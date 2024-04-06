from django import forms
from .choices import *


class GenreForm(forms.Form):
    OPTIONS = GENRES
    Genres = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS
    )
