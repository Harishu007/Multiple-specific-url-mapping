from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(request):
    return HttpResponse('<marquee>king is no1 batsemen</marquee>')
def abd(request):
    return HttpResponse('mr.360')
