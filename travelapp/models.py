from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from authapp.models import Instructor


class RouteType(models.IntegerChoices):
    ON_FOOT = 1, _('Пеший')
    ON_BIKE = 2, _('Велосипедный')
    ON_BOAT = 3, _('Водный')


class RouteLevel(models.IntegerChoices):
    EASY = 1, _('Простой')
    ADVANCED = 2, _('Продвинутый')
    HARD = 3, _('Сложный')


class RouteFilterQuerySet(models.QuerySet):
    def search(self, *args, **kwargs):
        qs = self.filter(is_active=True)
        if kwargs.get('name', ''):
            qs = qs.filter(name__icontains=kwargs['name'])
        if kwargs.get('region', ''):
            qs = qs.filter(location__icontains=kwargs['region'])
        if kwargs.get('type', ''):
            qs = qs.filter(type=kwargs['type'])
        if kwargs.get('level', ''):
            qs = qs.filter(complexity=kwargs['level'])

        return qs


class Route(models.Model):
    objects = RouteFilterQuerySet.as_manager()

    name = models.CharField(verbose_name='Название маршрута', max_length=100, unique=True)
    type = models.IntegerField(verbose_name='Тип маршрута',
                               choices=RouteType.choices,
                               default=RouteType.ON_FOOT,
                               db_index=True)
    base_price = models.DecimalField(verbose_name='Ориентировочная стоимость прохождения маршрута',
                                     max_digits=8,
                                     decimal_places=2,
                                     default=0)
    short_desc = models.TextField(verbose_name='Краткое описание')
    long_desc = models.TextField(verbose_name='Полное описание')
    location = models.CharField(verbose_name='Местоположение', max_length=200, db_index=True)
    duration = models.IntegerField(verbose_name='Продолжительность', db_index=True)
    length = models.FloatField(verbose_name='Длина', db_index=True)
    complexity = models.IntegerField(verbose_name='Сложность',
                                     choices=RouteLevel.choices,
                                     default=RouteLevel.EASY,
                                     db_index=True)
    added_at = models.DateTimeField(verbose_name='Время создания маршрута', auto_now_add=True)
    featured_photo = models.ImageField(upload_to='static/img', verbose_name='Фото для оформления маршрута', blank=True)
    is_active = models.BooleanField(verbose_name='Маршрут доступен для проведения', default=True, db_index=True)
    instructor = models.ForeignKey(Instructor,
                                   related_name='routes',
                                   on_delete=models.SET_NULL,  # todo ?
                                   null=True,
                                   db_index=True)
    # height_difference
    # times_run
    # comments

    def __str__(self):
        return f'Маршрут "{self.name}"\n{self.location} ({self.type}, {self.length:.1f}км, {self.duration}ч)\n' \
               f'Сложность: {self.complexity}'


class RoutePhoto(models.Model):
    image = models.ImageField(upload_to='static/route_photos')
    added_at = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    route = models.ForeignKey(Route, related_name='photos', on_delete=models.CASCADE)


class Trip(models.Model):
    route = models.ForeignKey('Route',
                              related_name='trips',
                              on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Стоимость прохождения маршрута',
                                max_digits=8,
                                decimal_places=2,)
    announced_at = models.DateTimeField(verbose_name='Время объявления похода', auto_now_add=True)
    starts_at = models.DateTimeField(verbose_name='Время начала похода')
    instructor = models.ForeignKey(Instructor,
                                   related_name='trips',
                                   on_delete=models.CASCADE)
    subbed = models.IntegerField(verbose_name='Мест занято', default=0)
    max_group_size = models.IntegerField(verbose_name='Количество мест', null=True)

    def get_cost(self):
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
