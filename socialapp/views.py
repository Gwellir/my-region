from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from rest_framework import viewsets

from authapp.decorators import traveler_only
from socialapp.forms import TripCommentCreateForm
from socialapp.models import CommentPhoto, TripComment
from socialapp.serializers import TripCommentRetrieveSerializer, TripCommentSerializer
from travelapp.models import Trip


# todo check for user participation
@method_decorator([login_required, traveler_only], name="dispatch")
class TripCommentCreate(CreateView):
    model = TripComment
    form_class = TripCommentCreateForm
    success_url = reverse_lazy("travelapp:route_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Создать комментарий к походу"

        return data

    def get_initial(self):
        return {
            "trip": Trip.objects.select_related().get(pk=self.kwargs["pk"]),
        }

    def get_form(self, form_class=None):
        form = super(TripCommentCreate, self).get_form(form_class)
        form.fields["trip"].disabled = True
        form.fields["photos"].required = False
        return form

    def form_valid(self, form):
        files = self.request.FILES.getlist("photos")
        form.instance.author = self.request.user
        form.cleaned_data.pop("photos")
        with transaction.atomic():
            result = super(TripCommentCreate, self).form_valid(form)
            for photo in files:
                CommentPhoto.objects.create(image=photo, comment=form.instance)

        return result


class TripCommentViewSet(viewsets.ModelViewSet):
    """
    Automatically provides list, create, retrieve, update and destroy actions.
    """

    queryset = TripComment.objects.filter(is_active=True, is_allowed=True)
    serializer_classes = {
        "retrieve": TripCommentRetrieveSerializer,
    }
    default_serializer_class = TripCommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
