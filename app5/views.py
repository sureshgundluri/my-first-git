from django.shortcuts import render
from django.http import HttpResponse
def sanvi(request):
    return HttpResponse('<h1>sanvika is a good girl</h1>')
def realme(request):
    return HttpResponse('<marquee><h1>one of the best mobile brand</h1></marquee>')
