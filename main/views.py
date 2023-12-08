from django.shortcuts import render, redirect
from .models import *
from .form import Registration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def main(request):
    prop_value = Products.objects.all()
    return render(request, 'main.html',{'prop_key':prop_value})

def about(request):
    return render(request,'about.html')

def register(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            login (request, user)
            return redirect ('Home')
        else:
            messages.error (request, 'Form is not correct')
    return render (request,'register.html', {'form':form})

