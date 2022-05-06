from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class User(models.Model):
    """Core of a user, contains basic datas from "sign up / register a new User" """
    name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    status_log = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # favorite_product =  models.ForeignKey(Product, on_delete=CASCADE)
    profile_image = models.CharField(max_length=9999)


class UserAccount(models.Model):
    """To store extra data from checkout, when user buys something.
     This is official data, so not to display on profile,
     and different name than login username as well."""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    # official name is probably different than username
    street_name = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.FloatField()
