from django.contrib.auth.forms import UserCreationForm, User
from django.shortcuts import render, redirect
from product.models import Product
from user.models import Profile, UserProfile, UserPayment, UserAddress
from django.db import models


# Create your views here.
def index(request):
    context = {'users': User.objects.all().order_by('name')}
    return render(request, 'user/index.html', context={'users': 'users'})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


# Something from the video 8 around 30'
# to filter product by name (return an array)
# def index(request):
#    Product.objects.filter(name__icontains=)
#    return render(request, 'user/index.html')