from django.forms import ModelForm, widgets, forms
#from django_countries.countries import COUNTRIES

from cart.models import Address, Payment

class CheckOutFormAddreess(ModelForm):
    class Meta:
        model = Address
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipcode': widgets.TextInput(attrs={'class': 'form-control'}),
            #'country': forms.ChoiceField(COUNTRIES),
        }


class CheckOutFormPayment(ModelForm):
    class Meta:
        model = Payment
        exclude = []
        widgets = {
            'card_holder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'expiry_dare': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc_number': widgets.TextInput(attrs={'class': 'form-control'})
        }




