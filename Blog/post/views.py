from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def Home(request):
    if request.user.is_authenticated and request.user.is_staff:
        print("user is logged in",request.user.username)
        form = "<input name='username'/>"
        return render(request,template_name='index.html',context={"form":form})
    return HttpResponse("not permitted",status=400)

def Featured(request):
    return render(request,template_name='feature.html')


def Price(request):
    return render(request,template_name='list.html')

def Blog(request):
    return render(request,template_name='list.html')

def BlogDetails(request):
    return render(request,template_name='list.html')

def Contact(request):
    return render(request,template_name='list.html')

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


 

   