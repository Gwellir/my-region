import json
import os

# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from authapp.models import AppUser, Instructor, Traveler
from travelapp.models import District, Region, Route, Trip, TripOptionAvailable

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
        # super_user = AppUser.objects.create_superuser('django', 'test@test.app', 'geekbrains', is_instructor=False)
        # super_user.save()

        # instructors = load_from_json('instructors')
        # for instructor in instructors:
        #     user = AppUser(**instructor['user'])
        #     user.save()
        #     instructor.pop('user', None)
        #     new_instructor = Instructor(user=user, **instructor)
        #     new_instructor.save()
        #
        # routes = load_from_json('routes')
        # for route in routes:
        #     instructor = AppUser.objects.get(instructor__pk=route['instructor_id']).instructor
        #     route.pop('instructor_id', None)
        #     print(instructor)
        #     new_route = Route(instructor=instructor, **route)
        #     new_route.save()
        #
        # trips = load_from_json('trips')
        # for trip in trips:
        #     route = Route.objects.get(pk=trip['route_id'])
        #     trip.pop('route_id', None)
        #     new_trip = Trip(route=route, instructor=route.instructor, **trip)
        #     new_trip.save()
