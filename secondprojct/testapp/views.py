from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def good_morning_view(request):
    return HttpResponse("<h1>hllo good morning</h1>")
def good_aftrnoon_view(request):
    return HttpResponse("<h1>hllo good afternoon</h1>")
def good_night_view(request):
    return HttpResponse("<h1>hllo good night</h1>")
def good_evening_view(request):
    return HttpResponse("<h1>hllo good evnening</h1>")

