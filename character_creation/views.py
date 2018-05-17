from django.shortcuts import render
from django.http import HttpResponse

def creation(request):
    return HttpResponse("The character creation screen")
