from django import forms
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from rest_framework import viewsets

from authapp.decorators import traveler_only
from ordersapp.models import Order, OrderItem
from ordersapp.permissions import OwnsOrIsTravelerOrReadOnly
from ordersapp.serializers import OrderSerializer
from travelapp.models import Trip, TripOptionAvailable
from utils.mail import send_instructor_notification, send_traveler_notification


@method_decorator([login_required, traveler_only], name='dispatch')
class OrderCreate(CreateView):
    """
    Страница с формой бронирования мест.
    """
    model = OrderItem
    # form_class = OrderItemForm
    success_url = reverse_lazy('travelapp:route_list')
    fields = ['trip', 'adults_amount', 'kids_amount', 'options_used', 'contact_phone', 'contact_email', 'notes']

    def get_initial(self):
        """
        Вводит информацию пользователя (по умолчанию) в поля формы.
        """
        return {
            'trip': Trip.objects.select_related().get(pk=self.kwargs['pk']),
            'contact_phone': self.request.user.phone,
            'contact_email': self.request.user.email,
        }

    def get_form(self, form_class=None):
        """
        Дополнительно настраивает параметры полей формы.
        """
        form = super(OrderCreate, self).get_form(form_class)
        form.fields['trip'].disabled = True
        form.fields['options_used'].required = False
        form.fields['options_used'].queryset = TripOptionAvailable.objects.filter(trip=form.initial['trip'])
        return form

    @transaction.atomic
    def form_valid(self, form):
        """
        Проверка данных формы (количество людей в группе) и обновление данных похода.
        """
        form_obj = form.save(commit=False)
        user = self.request.user
        form_obj.traveler = user.traveler
        trip = form_obj.trip
        trip.kids += form_obj.kids_amount
        trip.adults += form_obj.adults_amount
        if form_obj.trip.subbed > form_obj.trip.max_group_size:
            form.add_error('adults_amount', forms.ValidationError('Количество людей в заявке превышает количество оставшихся мест!'))
            form.add_error('kids_amount', forms.ValidationError('Количество людей в заявке превышает количество оставшихся мест!'))
            return super(OrderCreate, self).form_invalid(form)

        trip.save()
        form_obj.save()

        send_instructor_notification(form_obj)
        send_traveler_notification(form_obj)

        return super(OrderCreate, self).form_valid(form)


class OrderViewSet(viewsets.ModelViewSet):
    """
    Реализует СRUD для объектов брони (OrderItem)
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [OwnsOrIsTravelerOrReadOnly]

    def get_queryset(self):
        """
        Возвращает только релевантные элементы из списка заказов
        :return:
        """
        user = self.request.user
        if user.is_traveler:
            return OrderItem.objects.filter(traveler=user.traveler)
        elif user.is_instructor:
            return OrderItem.objects.filter(trip__instructor=user.instructor)
        else:
            return self.queryset

    def perform_create(self, serializer):
        serializer.save(traveler=self.request.user.traveler)
