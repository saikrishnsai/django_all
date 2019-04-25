from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting_info(request):
    return HttpResponse('<h1>good mornig</h1>')