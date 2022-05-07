from django.contrib.auth.models import User
from django.db import models
from product.models import Product
# from django_countries.fields import CountryField


# we can not use "User" as it's an inbuilt model in Django
# so I renamed it Profile because no other idea... /Sophie
class Profile(models.Model):
    """Core of a user, contains basic datas from "sign up / register a new User" """
    name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    # status_log = models.BooleanField(default=False)


class UserProfile(models.Model):
    """Contains extra info that are going to be display in the profile.
    A user can exist without a picture, so it's a different class."""
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # favorite_product =  models.ForeignKey(Product, on_delete=CASCADE)
    profile_image = models.CharField(max_length=9999)


class UserAddress(models.Model):
    """To store extra data from checkout, when user buys something.
     This is official data, so not to display on profile,
     and different name than login username as well."""
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    # official name is probably different than username
    street_name = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=999)
    # country = models.CountryField() # import causes error???
    zipcode = models.FloatField()


class UserPayment(models.Model):
    """To store the specific payment information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=26)
    expiry_date = models.DateField(max_length=10)
    cvc_number = models.IntegerField()
    # not sure if it's allowed to store that, but this is dummy so ok I guess
