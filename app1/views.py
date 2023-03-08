from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_app1(request):
    return HttpResponse('shahida is cute girl')


def second_app1(request):
    return HttpResponse('yashu is good girl')