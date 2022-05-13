from django.contrib.auth.models import User
from django.db import models
from user.models import Profile
from product.models import Product
from django_countries.fields import CountryField


class Address(models.Model):
    """To store extra data from checkout, when user buys something.
     This is official data, so not to display on profile,
     and different name than login username as well."""
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    # official name is probably different than username
    street_name = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    # country = models.CharField(choices=Countries, max_length=100)
    country = CountryField(blank_label='(select country)')
    zipcode = models.FloatField()


class Payment(models.Model):
    """To store the specific payment information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=26)
    expiry_date = models.DateField(max_length=10)
    cvc_number = models.IntegerField()
    # not sure if it's allowed to store that, but this is dummy so ok I guess

#class Orderreview(models.Model):
#    """to store the order and display order review"""
#    item = models.ForeignKey(Product, on_delete=models.CASCADE)
#    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
#    information = models.ForeignKey(Address, on_delete=models.CASCADE)