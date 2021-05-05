from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from time import sleep
from django.http import Http404

# Create your views here.


def Home(request):
    raise Http404()
    # return render(request,template_name='list.html')


# git add .
# git commit -m "i added templates"
# git push

# git pull


def Detail(request,id):
    raise Http404()
    return render(request,template_name='detail.html')


def Post(request,id):
    return render(request,template_name='post.html')


   