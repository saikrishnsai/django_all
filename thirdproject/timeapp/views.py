from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_info(request):
    time=datetime.datetime.now()
    return HttpResponse(str(time))
