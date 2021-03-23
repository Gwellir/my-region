from django.contrib import admin
from authapp.models import Instructor, Traveler, AppUser

# Register your models here.

admin.site.register(AppUser)
admin.site.register(Instructor)
admin.site.register(Traveler)
