from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from product.models import Product


# user = [
#    {'name': 'Kristbjörg', 'kristbjorge21@ru.is'}
# ]

# Create your views here.
def index(request):
    return render(request, 'user/index.html')


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