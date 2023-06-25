from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = "auth/UserRegister.html"
    success_url = reverse_lazy("login")


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = "auth/Login.html"

    # success_url = reverse_lazy("home")
    def get_success_url(self):
        return reverse_lazy("home")
