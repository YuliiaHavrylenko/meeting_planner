from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse('Welcome To The Meeting Planner Application')


def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")

def about(request):
    return HttpResponse("My name is Volt")