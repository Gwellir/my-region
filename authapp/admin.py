from django.contrib import admin

from authapp.models import AppUser, Instructor, Traveler

# Register your models here.

admin.site.register(AppUser)
admin.site.register(Instructor)
admin.site.register(Traveler)
