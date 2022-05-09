from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class ProductCategory(models.Model):
#    name_category = models.CharField(max_length=999)

#    def __str__(self):
#        return self.name_category


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    long_description = models.TextField(max_length=999, blank=True)
    # product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    on_sale = models.BooleanField(default=True)
    price = models.FloatField()
    # highest_offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
