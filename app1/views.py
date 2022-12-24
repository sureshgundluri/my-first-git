from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jspiders(request):
    return HttpResponse('<marquee><h1>jspiders is the best software training institute in banglore</h1></marquee>')
def suresh(request):
    return HttpResponse('<marquee direction="down"><h1>suresh is a talented person</h></marquee>')
