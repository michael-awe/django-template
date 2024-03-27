from django import forms


class GenreForm(forms.Form):
    OPTIONS = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Animation", "Animation"),
        ("Comedy", "Comedy"),
        ("Crime", "Crime"),
        ("Documentary", "Documentary"),
        ("Drama", "Drama"),
        ("Family", "Family"),
        ("Fantasy", "Fantasy"),
        ("History", "History"),
        ("Horror", "Horror"),
        ("Music", "Music"),
        ("Mystery", "Mystery"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Science Fiction"),
        ("Thriller", "Thriller"),
        ("War", "War"),
        ("Western", "Western"),
    )
    Genres = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS
    )
