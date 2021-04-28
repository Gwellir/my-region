# todo scrap after switching to API

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from rest_framework import generics
from rest_framework.permissions import AllowAny

from authapp.forms import SignupForm, UserLoginForm
from authapp.models import AppUser
from authapp.serializers import RegisterSerializer
from utils.mail import send_verify_mail


def login_view(request):
    """
    Страница логина пользователя.
    """

    title = "login"

    login_form = UserLoginForm(data=request.POST or None)

    next = request.GET["next"] if "next" in request.GET.keys() else ""

    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if "next" in request.POST.keys() and request.POST["next"]:
                return HttpResponseRedirect(request.POST["next"])
            else:
                return HttpResponseRedirect(reverse_lazy("main"))

    content = {
        "title": title,
        "login_form": login_form,
        "next": next,
    }
    return render(request, "authapp/login.html", content)


def logout(request):
    """
    Страница логаута пользователя.
    """

    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


class RegisterView(TemplateView):
    """
    Страница перехода для регистрации разных типов пользователей.
    """

    template_name = "authapp/register.html"


class SignupView(CreateView):
    """
    Страница регистрации.
    """

    model = AppUser
    form_class = SignupForm
    template_name = "authapp/signup.html"

    def form_valid(self, form):
        user: AppUser = form.save()
        if send_verify_mail(user):
            print("Sent registration confirmation message")
            return HttpResponseRedirect(reverse("auth:login"))
        else:
            print("Confirmation message not sent, encountered an error")
            return HttpResponseRedirect(reverse("auth:login"))
        # login(self.request, user)
        # return redirect('main')


class TravelerSignupView(SignupView):
    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "traveler"
        return super().get_context_data(**kwargs)


class InstructorSignupView(SignupView):
    """
    Страница регистрации инструктора.
    """

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "instructor"
        return super().get_context_data(**kwargs)


def verify(request, email, activation_key):
    try:
        user: AppUser = AppUser.objects.filter(email=email).first()
        if user.activation_key == activation_key and not user.is_key_expired():
            user.is_active = True
            user.save()
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return render(request, "authapp/verification.html")
        else:
            print(f"error activating user: {user}")
            return render(request, "authapp/verification.html")
    except Exception as e:
        print(f"error activating user : {e.args}")
        return HttpResponseRedirect(reverse("main"))


# API
class APIRegisterView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
