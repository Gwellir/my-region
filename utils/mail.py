from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key],
    )

    title = f'Подтверждение аккаунта Мой Край для: {user.username}'
    message = f'Чтобы завершить активацию аккаунта {user.username} на сервисе "Мой Край",'\
              f'перейдите по этой ссылке:\n{settings.DOMAIN_NAME}{verify_link}'

    print(f'from: {settings.EMAIL_HOST_USER}, to: {user.email}')
    # todo this is VERY slow, either implement sending through postfix or try anymail
    return send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )