from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

class Home(View):
    template_name = 'home.html'

class About(View):
    template_name = 'about_html'