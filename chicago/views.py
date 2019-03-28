from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



def welcome(request):
    return HttpResponse("Welcome to chicago")


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('welcome')
