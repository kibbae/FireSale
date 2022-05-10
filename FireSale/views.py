from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.models import Product, ProductImage


# Create your views here.
def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context=context)



# Til að sjá ekki ef ekki loggaður inn
# @login_required
# def blabla():
# pass
