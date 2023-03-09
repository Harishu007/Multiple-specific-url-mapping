from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('dhoni is best captain in the world')
def jaddu(request):
    return HttpResponse('<marquee><h1>no1 all rounder in the world</h1></marquee>')