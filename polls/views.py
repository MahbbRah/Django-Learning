from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello World are you ready to move on orr not?")
