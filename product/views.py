from django.shortcuts import render, get_object_or_404, redirect
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from product.models import Product, ProductImage
from django.forms import ModelForm, widgets
from django import forms


# /products
def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context=context)


# products/3
def get_product_by_id(request, id):
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


# video 9
# products/create_product
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


# products/delete_product/4
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products') # need to redirect to the name '' registered in the views
# not a requirement, so let's see with that


# products/update_product/4
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data = request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('get_product_by_id', id = id)

    else:
        form = ProductUpdateForm(instance = instance)

    return render(request, 'product/update_product.html',{
        'form': form,
        'id': id
    })
