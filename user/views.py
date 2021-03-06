from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django.shortcuts import render, redirect
from product.models import Product
from user.forms.profile_form import ProfileForm
from user.models import Profile
from django.db import models


# Create your views here.
def index(request):
    # context = {'users': User.objects.all().order_by('name')}
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

@login_required
def edit(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })

