from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def info(request):
    dt=datetime.datetime.now()
    my_dict={'date':dt,'name':'saikrishna','age':25,'roll':1130118226}
    return render(request,'testapp/result.html',my_dict)
