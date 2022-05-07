from django.db import models
from user.models import Profile


# Create your models here.
class ProductCategory(models.Model):
    """CategoryProduct will be use for search and catalog.
    I guess we should have an array of choices of categories"""
    CATEGORY_OPTIONS = (
        ('Home', 'Home'),
        ('Clothes', 'Clothes'),
        ('Cars', 'Cars'),
        ('Pets', 'Pets'),
        ('High-tech', 'High-tech'),
    )
    # to be continued I guess
    # Todo : make category coherent with front end
    # name_category = models.CharField(choiceon_delete=models.CASCADE)s=CATEGORY_OPTIONS, max_length=100)
    name_category = models.CharField(max_length=999)

    def __str__(self):
        return self.name_category


class Product(models.Model):
    name = models.CharField(max_length=200)
    # description = models.CharField()
    long_description = models.TextField(max_length=999, blank=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)

    # condition = models.CharField()
    # featured_image = models.ImageField(upload_to='Images')
    # on_sale = models.BooleanField()
    # price = models.FloatField()


    # class ProductImage(models.Model):
    #   image = models.CharField(max_length=9999)
    #  product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
