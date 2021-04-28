from django.shortcuts import render

# Create your views here.
from socialapp.models import TripComment
from travelapp.forms import RouteFilterForm
from travelapp.models import Route


def main(request):
    """
    Филлер главной страницы.
    """

    title = "Travel Freely!"

    content = {
        "title": title,
        "route_list": Route.objects.filter(is_active=True),
        "comment_list": TripComment.objects.filter(is_allowed=True, is_active=True),
        "form": RouteFilterForm(),
    }

    return render(request, "mainsite/index.html", context=content)
