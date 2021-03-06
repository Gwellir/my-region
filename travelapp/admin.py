from django.contrib import admin

# Register your models here.
from travelapp.models import (
    District,
    Region,
    Route,
    RoutePhoto,
    Trip,
    TripOptionAvailable,
)

admin.site.register(Route)
admin.site.register(RoutePhoto)
admin.site.register(Trip)
admin.site.register(TripOptionAvailable)
admin.site.register(Region)
admin.site.register(District)
