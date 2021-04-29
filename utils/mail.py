from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from ordersapp.models import OrderItem


def send_verify_mail(user):
    verify_link = reverse(
        "auth:verify",
        args=[user.email, user.activation_key],
    )

    title = f"Подтверждение аккаунта Мой Край для: {user.username}"
    message = (
        f'Чтобы завершить активацию аккаунта {user.username} на сервисе "Мой Край",'
        f"перейдите по этой ссылке:\n{settings.DOMAIN_NAME}{verify_link}"
    )

    print(f"from: {settings.EMAIL_HOST_USER}, to: {user.email}")
    # todo this is VERY slow, either implement sending through postfix or try anymail
    return send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )


def send_traveler_notification(order: OrderItem) -> bool:
    route = order.trip.route
    instructor = order.trip.instructor
    usermail = order.traveler.user.email
    title = f"Уведомление о бронировании мест в походе (Мой Край)"
    message = (
        f"С вашего аккаунта на сервисе Мой Край были забронированы места в походе"
        f' по маршруту "{route.name}".\n\n'
        f"Информация о заказе:\n"
        f"Регион: {route.location}\n"
        f"Тип: {route.get_route_type_display()}\n"
        f"Даты: {str(order.trip.starts_at)[:10]} - {str(order.trip.ends_at)[:10]}\n"
        f"Инструктор: {instructor.user.get_full_name()}\n"
        f"Стоимость: {order.trip.get_cost()}"
        f"Места: {order.adults_amount} взрослых, {order.kids_amount} детей\n\n"
        f"Связь с инструктором:\n почта: {instructor.user.email}, телефон: {instructor.user.phone}"
    )

    return send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [order.contact_email],
        fail_silently=False,
    )


def send_instructor_notification(order: OrderItem) -> bool:
    route = order.trip.route
    user = order.traveler.user
    instructor = order.trip.instructor
    title = f"Уведомление о бронировании мест в походе (Мой Край)"
    message = (
        f"На сервисе Мой Край были забронированы места в Вашем походе"
        f' по маршруту "{route.name}".\n\n'
        f"Информация о заказе:\n"
        f"Даты: {str(order.trip.starts_at)[:10]} - {str(order.trip.ends_at)[:10]}\n"
        f"Пользователь: {user.get_full_name()}\n"
        f"Места: {order.adults_amount} взрослых, {order.kids_amount} детей\n\n"
        f'Комментарий: "{order.notes}"\n'
        f"Связь с пользователем:\n почта: {order.contact_email}, телефон: {order.contact_phone}"
    )

    return send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [instructor.user.email],
        fail_silently=False,
    )
