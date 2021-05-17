import hashlib
from random import random

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.utils.timezone import now
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authapp.models import AppUser, Instructor, Traveler
from utils.mail import send_verify_mail

UserModel = get_user_model()


# todo protect with CAPTCHA or throttling
class UserProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для процесса регистрации пользователей.
    """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=AppUser.objects.all())],
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = [
            "is_instructor",
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "password",
            "password2",
            "avatar",
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "date_of_birth": {"required": True},
            "is_instructor": {"required": True},
        }

    def validate(self, attrs):
        if attrs.get("password", None) != attrs.get("password2", None):
            raise serializers.ValidationError({"password": "Пароли не совпадают!"})
        dob = attrs.get("date_of_birth", None)
        if dob:
            delta = (
                now().year
                - dob.year
                - ((now().month, now().day) < (dob.month, dob.day))
            )
            if delta < 18:
                raise serializers.ValidationError(
                    {"date_of_birth": "Возраст должен быть более 18 лет."}
                )

        return attrs

    @transaction.atomic
    def update(self, instance, validated_data):
        # todo придумать как менять основополагающее поле e-mail
        # todo выглядит как костыль...
        validated_data.pop("is_instructor")
        pw = validated_data.pop("password", None)
        if pw:
            instance.set_password(pw)
        super().update(instance, validated_data)
        return instance

    @transaction.atomic
    def create(self, validated_data):
        user = AppUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            date_of_birth=validated_data["date_of_birth"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            gender=validated_data["gender"],
            avatar=validated_data["avatar"],
        )
        user.set_password(validated_data["password"])

        if not validated_data["is_instructor"]:
            user.is_traveler = True
            profile_maker = Traveler
        else:
            user.is_instructor = True
            profile_maker = Instructor

        user.is_active = False
        salt = hashlib.sha1(str(random()).encode("utf8")).hexdigest()[:6]
        user.activation_key = hashlib.sha1(
            (user.email + salt).encode("utf8")
        ).hexdigest()
        user.save()

        profile = profile_maker.objects.create(user=user)
        if self.validated_data.get("about"):
            profile.about = self.validated_data.get("about")
        if self.validated_data.get("home_region"):
            profile.home_region = self.validated_data.get("home_region")
        profile.save()

        # todo try to understand how actions should be spread between logic layers,
        #  maybe send mail in post_save receiver?
        send_verify_mail(user)

        return user
