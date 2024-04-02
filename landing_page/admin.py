from django.contrib import admin
from recommendations.models import Movie

# Register your models here.
admin.site.register(Movie, admin.ModelAdmin)
