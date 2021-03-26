from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from authapp.decorators import traveler_only
from authapp.models import Instructor, Traveler


class InstructorList(ListView):
    model = Instructor


class InstructorDetail(DetailView):
    model = Instructor


class TravelerDetailView(DetailView):
    model = Traveler
    template_name = 'userapp/traveler_detail.html'


@method_decorator([login_required, traveler_only], name='dispatch')
class TravelerProfileView(DetailView):
    model = Traveler
    template_name = 'userapp/traveler_profile.html'
    context_object_name = 'traveler'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.request.user.traveler.pk)


class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'userapp/instructor_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.request.user.instructor.pk)
