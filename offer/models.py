from django.db import models
from product.models import Product
from user.models import Profile

# Create your models here.


class Offer(models.Model):
    """To store data when a potential buyer wants to bid on a product.
    Need to be linked to the Product, then by reference to the seller (I guess???)"""
    price = models.FloatField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.price
        # we need to return only the price to display + to create a sale if offer is_accepted


