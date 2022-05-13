from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from product.models import Product, ProductImage


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
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

