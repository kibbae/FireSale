from django.shortcuts import render

products = [
    {'name': 'Hlaupaskór', 'price': 5000, 'description': 'mjúkir og góðir', 'long_description': 'æðislega góðir skór í hlaup' },
    {'name': 'Inniskór', 'price': 1000, 'description': 'góðir', 'long_description': 'ver þig fyrir lego kubbum' }
]


# Create your views here.
def index(request):
    return render(request, 'product/index.html', context={'products':products})