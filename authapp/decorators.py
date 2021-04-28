from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def traveler_only(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="authapp:login"
):
    """
    Проверяет, является ли пользователь, обращающийся к виду, путешественником,
    в ином случае перенаправляет на страницу логина.
    """

    decorator = user_passes_test(
        lambda user: user.is_active and user.is_traveler,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return decorator(function)
    return decorator


def instructor_only(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="authapp:login"
):
    """
    Проверяет, является ли пользователь, обращающийся к виду, инструктором,
    в ином случае перенаправляет на страницу логина.
    """

    decorator = user_passes_test(
        lambda user: user.is_active and user.is_instructor,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return decorator(function)
    return decorator
