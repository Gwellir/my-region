import hashlib
from random import random

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django.utils.timezone import now

from authapp.models import AppUser, Traveler, Instructor


class UserLoginForm(AuthenticationForm):
    """
    Форма логина пользователя.
    """

    class Meta:
        model = AppUser
        fields = ('username', 'password')


class SignupForm(UserCreationForm):
    """
    Форма регистрации пользователя.
    """

    about = forms.CharField(required=True)
    home_region = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'gender', 'date_of_birth', 'password1', 'password2', 'avatar']

    def clean_date_of_birth(self):
        """
        Возвращает дату рождения пользователя из формы.

        Передаёт в форму ошибку в случае, если пользователю меньше 18 лет.
        """
        dob = self.cleaned_data['date_of_birth']
        delta = now().year - dob.year - ((now().month, now().day) < (dob.month, dob.day))
        if delta < 18:
            self.add_error('date_of_birth', forms.ValidationError('Вам должно быть более 18 лет!'))

        return dob

    @transaction.atomic
    def save(self):
        """
        Сохраняет данные формы для пользователя Django.

        Устанавливает тип пользователя и создаёт его профиль.
        """
        user = super().save(commit=False)
        user_type = self.data.get('user_type', None)
        if user_type == 'traveler':
            user.is_traveler = True
            profile_maker = Traveler
        elif user_type == 'instructor':
            user.is_instructor = True
            profile_maker = Instructor

        user.is_active = False
        salt = hashlib.sha1(str(random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        profile = profile_maker.objects.create(user=user)

        # print(self.cleaned_data)
        profile.about = self.cleaned_data.get('about')
        profile.home_region = self.cleaned_data.get('home_region')
        profile.save()
        return user
