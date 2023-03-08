from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_app2(request):
    return HttpResponse('my mon is my inspiraration')

def second_app2(request):
    return HttpResponse('my dad is my bestfriend')

