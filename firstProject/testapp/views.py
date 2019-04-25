from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.



def datetime_view(request):
    date = datetime.datetime.now()
    s = '<h1>the current date and time is:' + str(date) + '</h1>'
    return HttpResponse(s)
