from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import Registration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Animal
from .models import Category
from .models import Order
from .form import DonationForm, VolunteerApplicationForm

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
    orders = Order.objects.all()
    new_orders = []
    for item in orders:
        if item.customer == request.user:
            new_orders.insert(0, item)
    if request.method == 'POST':
        if request.POST.get('del'):
            current_orders = Order.objects.get(id=request.POST.get('del'))
            current_orders.delete()
        else:
            print(request.POST.get('del'))
    data = {
        'orders': new_orders,
        'not_null': len(new_orders)
    }

    return render(request, 'profile.html', data)


def adoption(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    animals = Animal.objects.filter(category__title__icontains=q)
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart_obj = Order.objects.create(customer=request.user)
            added = Animal.objects.filter(id=request.POST.get('prod'))
            cart_obj.animals.set(added)
        else:
            return redirect('sign-in')
    return render(request,'adoption.html', {'categories': categories, 'animals': animals})



def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Donate')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def volunteer(request):
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Volunteer')
    else:
        form = VolunteerApplicationForm()
    return render(request, 'volunteer.html', {'form': form})