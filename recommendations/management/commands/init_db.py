"""
This file holds the functionality for initializing the database with the data from a JSON fixture file.
It was created in order to speed up the process of loading data into the database via the bulk_create
call as the original JSON file's size made the loaddata command slow. It is kept for posterity/reference.
"""

import json
from django.core.management.base import BaseCommand
from django.db import transaction
from recommendations.models import Movie


class Command(BaseCommand):
    help = "Loads data from a JSON fixture file into the database efficiently"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str, help="Path to the JSON fixture file")

    def handle(self, *args, **kwargs):
        print("The database has already been initialized!")
        return
        file_path = kwargs["json_file"]
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            movies_to_create = []
            for entry in data:
                fields = entry["fields"]
                movie = Movie(
                    name=fields.get("name"),
                    year=fields.get("year"),
                    genres=fields.get("genres"),
                    runtime=fields.get("runtime"),
                    language=fields.get("language"),
                    budget=fields.get("budget"),
                    revenue=fields.get("revenue"),
                    poster=fields.get("poster"),
                    overview=fields.get("overview"),
                    tagline=fields.get("tagline"),
                    starring=fields.get("starring"),
                    director=fields.get("director"),
                    writer=fields.get("writer"),
                    cinematographer=fields.get("cinematographer"),
                    composer=fields.get("composer"),
                    watch_providers=fields.get("watch_providers"),
                    keywords=fields.get("keywords"),
                    tmdb_id=fields.get("tmdb_id"),
                    imdb_rating=fields.get("imdb_rating"),
                    imdb_votes=fields.get("imdb_votes"),
                )
                movies_to_create.append(movie)
            with transaction.atomic():
                Movie.objects.bulk_create(movies_to_create)
            print("Data loaded successfully")
        except Exception as e:
            print(e)
