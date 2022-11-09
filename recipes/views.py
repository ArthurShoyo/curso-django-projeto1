from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('home 1')


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')
