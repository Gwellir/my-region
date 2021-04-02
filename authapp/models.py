from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

from ordersapp.models import OrderItem


class Gender(models.IntegerChoices):
    """
    Варианты выбора пола.
    """

    FEMALE = 1, _('Женский')
    MALE = 2, _('Мужской')


def get_expiry_datetime():
    return now() + timedelta(hours=24)


def email_is_lowercase(mail):
    if not isinstance(mail, str) or mail != mail.lower():
        raise ValidationError(_(f'Укажите адрес почты в нижнем регистре!'))


class AppUser(AbstractUser):
    """
    Модель пользователя Django.
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    avatar = models.ImageField(upload_to='static/user_pics', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', default=now)
    activation_key = models.CharField(verbose_name='Ключ активации', max_length=128, blank=True)
    activation_key_expiry = models.DateTimeField(
        verbose_name='Крайний срок текущей активации',
        default=get_expiry_datetime,
    )
    gender = models.IntegerField(verbose_name='Пол', blank=False, db_index=True, choices=Gender.choices)
    phone = models.CharField(verbose_name='Номер телефона', blank=True, max_length=20)
    email = models.EmailField(verbose_name='Адрес Email',
                              unique=True,
                              validators=[email_is_lowercase])
    is_instructor = models.BooleanField(default=False, null=False, db_index=True)
    is_traveler = models.BooleanField(default=False, null=False, db_index=True)
    # phone_number

    def is_key_expired(self) -> bool:
        """
        Проверка на время активности ключа активации.
        """
        if now() <= self.activation_key_expiry:
            return False
        else:
            return True

    @property
    def role_display(self):
        if self.is_superuser or self.is_staff:
            return 'Админ'
        elif self.is_instructor:
            return 'Гид'
        elif self.is_traveler:
            return 'Походник'
        else:
            return 'Н/Д'

    def __str__(self):
        return f'[{self.get_gender_display()[:1]}] {self.username} ({self.role_display})'


class Traveler(models.Model):
    """
    Модель профиля путешественника.
    """
    user = models.OneToOneField(AppUser, unique=True, db_index=True, null=False, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='О себе', blank=True, default='Обо мне')
    home_region = models.CharField(verbose_name='Место проживания', max_length=100, blank=True, null=True)
    following = models.ManyToManyField('Instructor', verbose_name='Подписки', blank=True, related_name='followers')
    trips_completed = models.ManyToManyField('travelapp.Trip', verbose_name='Походы', related_name='participants')

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.home_region})'

    # todo: implement a model manager
    def get_planned_trips(self):
        """
        Возвращает выборку запланированных поездок.
        """
        return OrderItem.objects.filter(trip__starts_at__gte=now(), traveler=self)

    # todo вероятно, не требуется
    def get_active_trips(self):
        """
        Возвращает выборку текущих поездок.
        """
        return OrderItem.objects.filter(trip__starts_at__lte=now(),
                                        trip__ends_at__gte=now(),
                                        traveler=self,
                                        )

    def get_finished_trips(self):
        """
        Возвращает выборку завершённых поездок пользователя.
        """
        return OrderItem.objects.filter(trip__ends_at__lte=now(), traveler=self)


class Instructor(models.Model):
    """
    Модель профиля инструктора.
    """
    user = models.OneToOneField(AppUser, unique=True, db_index=True, null=True, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='О себе', blank=True, default='Обо мне')
    home_region = models.CharField(verbose_name='Место проживания', max_length=100, blank=True, null=True)
    trips_run = models.IntegerField(verbose_name='Пройдено маршрутов', default=0)
    # subscribers = models.ManyToManyField(Traveler, verbose_name='Подписчики', blank=True, related_name='subscribed_to')

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.home_region})'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
