from django.shortcuts import render, redirect

from cart.forms.cart_form import CheckOutFormAddreess, CheckOutFormPayment
from cart.models import Address, Payment

def index(request):
    if request.method == 'POST':
        form = CheckOutFormAddreess(data=request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            #address.name = User.id
            address.save()
            return redirect('payment')
    else:
        form = CheckOutFormAddreess()
    return render(request, 'cart/index.html', {
        'form': form
    })

def payment(request):
    if request.method == 'POST':
        form = CheckOutFormPayment(data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            return redirect('orderreview')
    else:
        form = CheckOutFormPayment()
    return render(request, 'cart/payment.html', {
        'form': form
    })

#def shipping(request):
 #   return render(request, 'cart/shipping.html')


def orderreviw(request):
    context = {'address': Address.objects.all().order_by('full_name')}
    return render(request, 'cart/orderrew.html', context)

