from django.db import transaction
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from travelapp.models import Route, RoutePhoto, Trip

from .filters import TripFilter
from .forms import RouteCreateForm, RouteFilterForm
from .permissions import OwnsOrIsInstructorOrReadOnly
from .serializers import RouteRetrieveSerializer, RouteSerializer, TripSerializer


class RouteList(ListView):
    model = Route

    def get_context_data(self, **kwargs):
        data = super(RouteList, self).get_context_data(**kwargs)
        form = RouteFilterForm()
        data["form"] = form
        data["title"] = "Список маршрутов"

        return data

    def get_queryset(self):
        if self.request.GET.items():
            form = RouteFilterForm(self.request.GET)
            if form.is_valid():
                return Route.objects.search(**form.cleaned_data)
        return Route.objects.filter(is_usable=True)


class TripSelectorList(ListView):
    model = Trip
    template_name = "travelapp/trip_selector.html"
    context_object_name = "trip_list"

    def get_context_data(self, **kwargs):
        data = super(TripSelectorList, self).get_context_data(**kwargs)
        form = RouteFilterForm()
        data["title"] = "Выбрать поход"
        data["form"] = form
        data["route_list"] = Route.objects.all()[:6]

        return data

    def get_queryset(self):
        if self.request.GET.items():
            form = RouteFilterForm(self.request.GET)
            if form.is_valid():
                return Trip.objects.get_filtered(**form.cleaned_data)


class RouteDetail(DetailView):
    model = Route


class RouteCreateView(CreateView):
    model = Route
    form_class = RouteCreateForm
    success_url = reverse_lazy("travelapp:route_list")

    def form_valid(self, form):
        files = self.request.FILES.getlist("photos")
        form.instance.instructor = self.request.user.instructor
        form.cleaned_data.pop("photos")
        with transaction.atomic():
            result = super(RouteCreateView, self).form_valid(form)
            for photo in files:
                RoutePhoto.objects.create(image=photo, route=form.instance)

        return result


class TripDetail(DetailView):
    model = Trip


class RouteViewSet(viewsets.ModelViewSet):
    """
    Реализует СRUD для объектов маршрутов (Route)
    """

    queryset = Route.objects.filter(is_active=True, is_checked=True)
    serializer_classes = {
        "retrieve": RouteRetrieveSerializer,
    }
    default_serializer_class = RouteSerializer
    permission_classes = [OwnsOrIsInstructorOrReadOnly]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user.instructor)


class TripViewSet(viewsets.ModelViewSet):
    """
    Реализует СRUD для объектов походов (Trip)
    """

    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [OwnsOrIsInstructorOrReadOnly]
    filterset_class = TripFilter

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user.instructor)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "routes": reverse("route-list", request=request, format=format),
        }
    )
