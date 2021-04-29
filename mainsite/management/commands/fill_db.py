import json
import os

from django.core.management.base import BaseCommand

from authapp.models import AppUser, Instructor
from travelapp.models import Route, Trip

JSON_PATH = "mainsite/json"


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + ".json"), "r") as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = "Fill DB with new data"

    def handle(self, *args, **options):
        Trip.objects.all().delete()
        Route.objects.all().delete()
        Instructor.objects.all().delete()
        AppUser.objects.all().delete()
