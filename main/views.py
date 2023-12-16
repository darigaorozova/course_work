from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import Registration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Animal
from .models import Category

# Create your views here.
def main(request):
    prop_value = Animal.objects.all()
    return render(request, 'main.html',{'prop_key':prop_value})



def about(request):
    return render(request,'about.html')

def logout_user(request):
    logout(request)
    return redirect('Home')

#Sign In
def sign_in(request):
    page = 'signin'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Not correct')

    return render(request, 'register.html', {'page': page})

#Sign Up
def sign_up(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Error occurred')
    return render(request, 'register.html', {'form': form})
@login_required(login_url='Login')
def profile(request):
    return render(request, 'profile.html')

def adoption(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    animals = Animal.objects.filter(category__title__icontains=q)
    return render(request,'adoption.html', {'categories': categories, 'animals': animals})


