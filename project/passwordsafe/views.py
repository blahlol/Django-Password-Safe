from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save() 
            login(request,user)
            return redirect('safe:userpage')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('safe:userpage')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
    