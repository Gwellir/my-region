from django.db import models

# from authapp.models import Traveler
from travelapp.models import Trip, TripOptionAvailable


class Order(models.Model):
    pass


# todo as there is no basket, just make this an Order
class OrderItem(models.Model):
    """
    Модель, описывающая бронь мест клиентом
    """
    traveler = models.ForeignKey('authapp.Traveler', null=False, related_name='ordered_trips', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, verbose_name='Поход', null=False, related_name='ordered', on_delete=models.CASCADE, db_index=True)
    adults_amount = models.IntegerField(verbose_name='Взрослых в вашей группе', default=1, null=False)
    kids_amount = models.IntegerField(verbose_name='Детей в вашей группе', default=0, null=False)
    options_used = models.ManyToManyField(TripOptionAvailable, verbose_name='Дополнительные опции')
    contact_phone = models.CharField(verbose_name='Контактный телефон', max_length=15, null=False)
    contact_email = models.EmailField(verbose_name='Контактный E-mail', blank=False)
    notes = models.TextField(verbose_name='Пожелания', blank=True)

    class Meta:
        unique_together = (('traveler', 'trip'),)

    @property
    def get_group_size(self):
        return self.adults_amount + self.kids_amount
