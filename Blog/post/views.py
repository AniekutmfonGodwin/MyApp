from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from time import sleep

# Create your views here.


def Home(request):
    
    return render(request,template_name='list.html')





def Detail(request,id):
    return render(request,template_name='detail.html')


def Post(request,id):
    return render(request,template_name='post.html')


   