
from django.shortcuts import render, get_object_or_404, redirect

from product.forms.product_form import ProductCreateForm
from product.models import Product, ProductImage
from django.forms import ModelForm, widgets
from django import forms

#products = [
    #{'name': 'Hlaupaskór', 'price': 5000, 'description': 'mjúkir og góðir', 'long_description': 'æðislega góðir skór í hlaup' },
  #  {'name': 'Inniskór', 'price': 1000, 'description': 'góðir', 'long_description': 'ver þig fyrir lego kubbum' }
#]


# Create your views here.
def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context={'products':products})


def get_product_by_id(request, id):
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


# video 9
def create_product(request):
    if request.method == 'POST':
        form= ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image= request.POST['image'], product=product)
            product_image.save()
            return redirect(product-index)
    else:
        form= ProductCreateForm()
    return render(request, 'product/create_product.html',{
        'form': form
    })

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product-index')