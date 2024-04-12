from django import forms
from .choices import *


class GenreForm(forms.Form):
    Question = forms.CharField(
        initial="Let's pick your desired genre(s)!", disabled=True, max_length=50
    )

    OPTIONS = GENRES
    Genres = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS,
        help_text=(
            "Note: Your selected movie will have an element of all these genres "
            "so if you select 'romance' and 'comedy', we'll find rom-coms for you."
        ),
    )


class YearForm(forms.Form):
    Question = forms.CharField(
        initial="What release time frame are you feeling today?",
        disabled=True,
        max_length=50,
    )

    OPTIONS = YEAR_SPANS
    Years = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS
    )
