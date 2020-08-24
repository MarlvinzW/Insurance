from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings

"""
    LOGIN VIEW 
"""


class LoginView(View):
    template_name = 'pages/login.html'
    title = f"{settings.PLATFORM_NAME} | Login"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    def post(self, request, *args, **kwargs):
        pass


"""
    REGISTER VIEW 
"""


class RegistrationView(View):
    template_name = 'pages/register.html'
    title = f"{settings.PLATFORM_NAME} | Register"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})

    def post(self, request, *args, **kwargs):
        pass


"""
    HOME VIEW 
"""


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

