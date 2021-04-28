from django.contrib import admin

from socialapp.models import CommentPhoto, TripComment

admin.site.register(TripComment)
admin.site.register(CommentPhoto)
