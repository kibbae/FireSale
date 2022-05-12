# import timestamp as timestamp
from django.forms import ModelForm, widgets
from django import forms
from product.models import Product, Offer


# video 9

class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['id', 'highest_offer', 'available', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
        }


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id', 'highest_offer', 'available', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
        }


class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        exclude = ['id', 'item', 'buyer', 'timestamp', 'is_accepted']
        widgets = {
            'price': widgets.TextInput(attrs={'class': 'form-control', 'id':"item_id"})
        }
