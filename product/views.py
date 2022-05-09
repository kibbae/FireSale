from django.shortcuts import render, get_object_or_404
from product.models import Product

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