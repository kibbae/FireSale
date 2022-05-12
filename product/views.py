from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from product.forms.product_form import ProductCreateForm, ProductUpdateForm, MakeOfferForm
from product.models import Product, ProductImage
from django.forms import ModelForm, widgets
from django import forms


# /products
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        # products = list(Product.objects.filter(name__icontains=search_filter).values())
        return JsonResponse({'data': products})
    if 'order_by' in request.GET:
        split = request.GET['order_by'].split("_")
        field = split[0]
        order = split[1]
        if order == "asc":
            order = ""
        else:
            order = "-"
        print(order + field)
        context = {'products': Product.objects.all().order_by(order + field)}
        return render(request, 'product/index.html', context)
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)


# products/3
def get_product_by_id(request, id):
    product = get_object_or_404(Product, pk=id)
    # User is submitting a form
    if request.method == 'POST':
        form = MakeOfferForm(data=request.POST)
        # The form is valid
        if form.is_valid():
            offer = form.save(commit=False)
            offer.buyer = request.user
            offer.product = Product.objects.get(pk=id)
            offer.save()
            return redirect('products')

        # The form is invalid, send form back with errors
        return render(request, 'product/product_details.html', {
            'product': product,
            'form': form,
        })

    # Send empty form to user
    form = MakeOfferForm(initial={'price': product.price})
    return render(request, 'product/product_details.html', {
        'product': product,
        'form': form,
    })


# products/create_product
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            # return redirect(product-index)
            return redirect('products')
    else:
        form = ProductCreateForm()
    return render(request, 'product/create_product.html', {
        'form': form
    })


# products/delete_product/4
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products')  # need to redirect to the name '' registered in the views


# not a requirement, so let's see with that


# products/update_product/4
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            # return redirect('product-details', id = id)
            return redirect('products')
    else:
        form = ProductUpdateForm(instance=instance)

    return render(request, 'product/update_product.html', {
        'form': form,
        'id': id
    })


# products/make_offer/4
@login_required
def make_offer(request, id):
    # User is submitting a form
    if request.method == 'POST':
        form = MakeOfferForm(data=request.POST)
        # The form is valid
        if form.is_valid():
            offer = form.save(commit=False)
            offer.buyer = request.user
            offer.product = Product.objects.get(pk=id)
            offer.save()
            return redirect('products')

        # The form is invalid, send form back with errors
        return render(request, 'product/product_details.html', {
            'form': form,
            'id': id
        })

    # Send empty form to user
    form = MakeOfferForm()
    return render(request, 'product/product_details.html', {
        'form': form,
        'id': id
    })
