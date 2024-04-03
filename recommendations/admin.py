from django.contrib import admin
from .models import Movie

# Register your models here.

admin.site.register(Movie, admin.ModelAdmin)
