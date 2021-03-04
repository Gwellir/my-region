from django import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from authapp.decorators import traveler_only
from ordersapp.models import Order, OrderItem
from travelapp.models import Trip, TripOptionAvailable


@method_decorator([login_required, traveler_only], name='dispatch')
class OrderCreate(CreateView):
    model = OrderItem
    # form_class = OrderItemForm
    success_url = reverse_lazy('travelapp:route_list')
    fields = ['trip', 'adults_amount', 'kids_amount', 'options_used', 'contact_phone', 'contact_email', 'notes']

    def get_initial(self):
        return {
            'trip': Trip.objects.select_related().get(pk=self.kwargs['pk']),
            'contact_phone': self.request.user.phone,
            'contact_email': self.request.user.email,
        }

    def get_form(self, form_class=None):
        form = super(OrderCreate, self).get_form(form_class)
        form.fields['trip'].disabled = True
        form.fields['options_used'].required = False
        form.fields['options_used'].queryset = TripOptionAvailable.objects.filter(trip=form.initial['trip'])
        return form

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        user = self.request.user
        form_obj.traveler = user.traveler
        trip = form_obj.trip
        trip.kids += form_obj.kids_amount
        trip.adults += form_obj.adults_amount
        if form_obj.trip.subbed > form_obj.trip.max_group_size:
            raise forms.ValidationError('В группе набирается слишком много людей!')

        trip.save()
        form_obj.save()

        return super(OrderCreate, self).form_valid(form)
