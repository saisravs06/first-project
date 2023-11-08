from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sravs(request):
    return HttpResponse ('sweet')
def niha(request):
    return HttpResponse(' cute')
def arya(request):
    return HttpResponse(' hot')
def preethi(request):
    return HttpResponse(' mad')
def asha(request):
    return HttpResponse(' calm')
def dkds(request):
    return HttpResponse('<h1><marquee>we are forever</marquee></h1>')


