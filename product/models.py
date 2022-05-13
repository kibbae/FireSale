from django.contrib.auth.models import User
from django.db import models
from user.models import Profile

# Create your models here.


class ProductCategory(models.Model):
    name_category = models.CharField(max_length=999)

    def __str__(self):
        return self.name_category


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    long_description = models.TextField(max_length=999, blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='seller')
    # by default, for "create-product", the user seller will be id 1
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


class Offer(models.Model):
    """To store data when a potential buyer wants to bid on a product.
    Need to be linked to the Product, then by reference to the seller (I guess???)"""
    price = models.FloatField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='buyer')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.price
        # we need to return only the price to display + to create a sale if offer is_accepted


