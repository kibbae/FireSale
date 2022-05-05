from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #favorite_product =  models.ForeignKey(Product, on_delete=CASCADE)
    profile_image = models.CharField(max_length=9999)