from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

from auth_user.forms import AuthForm

""" выход пользователя из системы """

class LogOut(LogoutView) :
    template_name = "auth_user/auth.html"
    next_page = '/'

""" авторизация пользователя в системе """


class AuthenticationView(LoginView):
    template_name = 'auth_user/auth.html'
    form_class = AuthForm
    next_page = 'cabinet'


""" декоратор проверяющий авторизацию пользователя"""

def auth_decoration(func):
    def wraper(self, request):
        if not request.user.is_authenticated:
            return redirect('/')
        return func(self, request)
    return wraper


