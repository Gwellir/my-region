from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
# from authapp.models import Instructor
from socialapp.models import TripComment


class RouteType(models.IntegerChoices):
    ON_FOOT = 1, _('Пеший')
    ON_BIKE = 2, _('Велосипедный')
    ON_BOAT = 3, _('Водный')


class RouteLevel(models.IntegerChoices):
    EASY = 1, _('Простой')
    ADVANCED = 2, _('Продвинутый')
    HARD = 3, _('Сложный')


# todo this is actually bad
class TripFilterQuerySet(models.QuerySet):
    """
    Временная реализация функционала фильтрации походов для первого MVP.
    """
    def get_filtered(self, **kwargs):
        # todo: fix double query
        qs = self.filter(
            route__in=Route.objects.search(**kwargs),
            starts_at__gte=now(),
        )
        if kwargs.get('date_from', ''):
            qs = qs.filter(starts_at__gte=kwargs['date_from'])
        if kwargs.get('date_to', ''):
            qs = qs.filter(ends_at__lte=kwargs['date_to'])
        if kwargs.get('price_from', ''):
            qs = qs.filter(price__gte=int(kwargs['price_from']))
        if kwargs.get('price_to', ''):
            qs = qs.filter(price__lte=int(kwargs['price_to']))

        return qs


class RouteFilterQuerySet(models.QuerySet):
    """
    Временная реализация фильтра маршрутов для первого MVP
    """

    def search(self, *args, **kwargs):
        qs = self.filter(is_active=True, is_checked=True)
        if kwargs.get('region', ''):
            qs = qs.filter(location=kwargs['region'])
        elif kwargs.get('district', ''):
            qs = qs.filter(location__district=kwargs['district'])
        if kwargs.get('type', ''):
            qs = qs.filter(type=kwargs['type'])
        if kwargs.get('level', ''):
            qs = qs.filter(complexity=kwargs['level'])

        return qs


class Route(models.Model):
    """
    Модель маршрута.
    """

    objects = RouteFilterQuerySet.as_manager()

    name = models.CharField(verbose_name='Название маршрута', max_length=100, unique=True)
    route_type = models.IntegerField(verbose_name='Тип',
                                     choices=RouteType.choices,
                                     default=RouteType.ON_FOOT,
                                     db_index=True)
    base_price = models.DecimalField(verbose_name='Ориентировочная стоимость прохождения маршрута',
                                     max_digits=8,
                                     decimal_places=2,
                                     default=0)
    short_desc = models.TextField(verbose_name='Краткое описание')
    # todo implement richtextfield
    long_desc = models.TextField(verbose_name='Полное описание')
    # location = models.CharField(verbose_name='Местоположение', max_length=200, db_index=True)
    location = models.ForeignKey('travelapp.Region',
                                 verbose_name='Местоположение',
                                 db_index=True,
                                 null=True,
                                 on_delete=models.SET_NULL)
    duration = models.IntegerField(verbose_name='Продолжительность', db_index=True)
    length = models.FloatField(verbose_name='Длина', db_index=True)
    complexity = models.IntegerField(verbose_name='Сложность',
                                     choices=RouteLevel.choices,
                                     default=RouteLevel.EASY,
                                     db_index=True)
    added_at = models.DateTimeField(verbose_name='Время создания маршрута', auto_now_add=True)
    # todo implement proper working with photos, including thumbnailing
    featured_photo = models.ImageField(upload_to='static/img', verbose_name='Фото для оформления маршрута', blank=True)
    is_active = models.BooleanField(verbose_name='Маршрут доступен для проведения', default=True, db_index=True, blank=False)
    is_checked = models.BooleanField(verbose_name='Модерация проведена', default=False, db_index=True, blank=False)
    instructor = models.ForeignKey('authapp.Instructor',
                                   related_name='routes',
                                   on_delete=models.SET_NULL,  # todo ?
                                   null=True,
                                   db_index=True)
    # height_difference
    # times_run
    # comments

    def get_planned_trips(self):
        return Trip.objects.filter(route=self, starts_at__gte=now())

    def get_active_trips(self):
        return Trip.objects.filter(route=self,
                                   starts_at__lte=now(),
                                   ends_at__gte=now(),
                                   )

    def get_finished_trips(self):
        return Trip.objects.filter(route=self, ends_at__lte=now())

    def get_route_comments(self):
        return TripComment.objects.filter(trip__route=self)

    @property
    def is_usable(self):
        return self.is_checked and self.is_active

    def __str__(self):
        return f'Маршрут "{self.name}"\n{self.location} ({self.route_type}, {self.length:.1f}км, {self.duration}ч)\n' \
               f'Сложность: {self.complexity}'


class RoutePhoto(models.Model):
    """
    Модель сопроводительной фотографии маршрута.
    """
    image = models.ImageField(upload_to='static/route_photos')
    added_at = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    route = models.ForeignKey(Route, related_name='photos', on_delete=models.CASCADE)


class Trip(models.Model):
    """
    Модель похода, объявленного по связанному маршруту.
    """
    objects = TripFilterQuerySet.as_manager()
    route = models.ForeignKey('Route',
                              related_name='trips',
                              on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Стоимость прохождения маршрута',
                                max_digits=8,
                                decimal_places=2,)
    announced_at = models.DateTimeField(verbose_name='Время объявления похода', auto_now_add=True)
    starts_at = models.DateTimeField(verbose_name='Время начала похода', blank=False, db_index=True)
    ends_at = models.DateTimeField(verbose_name='Время окончания похода', blank=False, db_index=True)
    instructor = models.ForeignKey('authapp.Instructor',
                                   related_name='trips',
                                   on_delete=models.CASCADE)
    kids = models.IntegerField(verbose_name='Детей в группе', default=0)
    adults = models.IntegerField(verbose_name='Взрослых в группе', default=0)
    # subbed = models.IntegerField(verbose_name='Мест занято', default=0)
    max_group_size = models.IntegerField(verbose_name='Количество мест', null=True)

    @property
    def subbed(self):
        """
        Возвращает полное количество участников.
        """

        return self.kids + self.adults

    def get_cost(self):
        """
        Возвращает стоимость участия в походе (за одно место) с учётом опций
        """

        options_cost = 0
        for option in self.options.all():
            options_cost += option.price
        return self.price + options_cost

    def __str__(self):
        return f'Поход по маршруту "{self.route.name}" ({self.starts_at})'


class Options(models.IntegerChoices):
    INSURANCE = 1, _('Страховка')
    RENT = 2, _('Аренда инвентаря')
    FOOD = 3, _('Питание')
    LIVING_EXPENCES = 4, _('Проживание')
    TRANSIT = 5, _('Проезд до места')


class TripOptionAvailable(models.Model):
    """
    Модель описывает опции, которые организатор похода объявил доступными для этого похода.
    """

    trip = models.ManyToManyField('Trip',
                                  related_name='options',)
    name = models.IntegerField(verbose_name='Наименование опции',
                               choices=Options.choices,
                               )
    price = models.DecimalField(verbose_name='Стоимость опции',
                                max_digits=7,
                                decimal_places=2,
                                default=0)

    def __str__(self):
        return f'{self.get_name_display()}: {self.price} р.'


class District(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50, blank=False, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Region(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50, blank=False, db_index=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.district.name})'
