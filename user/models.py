from django.db import models


# Create your models here.
class User(models.Model):
    """Core of a user, contains basic datas from "sign up / register a new User" """
    name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    status_log = models.BooleanField(default=False)

    # does the following functions have to be here? Or in services?
    def log_in(self):
        self.is_log()

    def log_out(self):
        pass

    def is_log(self):
        self.status_log = True
        # don't return anything, change just a condition

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """To display info about the class User """

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='Images')
    bio = models.TextField(max_length=250)
    rating = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)

    # why PyCharl is complaining on reference ???

    def __str__(self):
        return self.name


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

    # information_payments --> let's see later on, as a bonus, if we decide to store it

    def __str__(self):
        return self.name


class Product(models.Model):
    """To store data from the seller when create a new product for sale.
    Initially named Item in the class diagram.
    Condition is organised as a fixed array of choices."""
    # todo make condition coherent with front end
    CONDITION_OPTIONS = (
        ('0', 'for parts'),
        ('1', 'condition very used'),
        ('2', 'ok condition'),
        ('3', 'very good condition'),
        ('4', 'like new'),
        ('5', 'New with tag'),
            )

    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField()
    long_description = models.TextField()
    #condition = models.CharField(choices=CONDITION_OPTIONS, max_length=25)
    #featured_image = models.ImageField(upload_to='Images')
    #timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    #is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CategoryProduct(models.Model):
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
    name_category = models.CharField(choices=CATEGORY_OPTIONS, max_length=100)

    def __str__(self):
        return self.name_category


class Offer(models.Model):
    """To store data when a potential buyer wants to bid on a product.
    Need to be linked to the Product, then by reference to the seller (I guess???)"""
    price = models.FloatField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.price
        # we need to return only the price to display + to create a sale if offer is_accepted


class SaleOrder(models.Model):
    price = models.ForeignKey(Offer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField()
    # or ForeignKey(Rating) ??? not sure here how to store / access rating

    # TODO check how to make it between 0 to 5

    def __str__(self):
        return self.rating
    # return rating to display it


class Rating(models.Model):
    """Not sure if we need a class for that but at the moment I don't know how to do other"""
    RATING_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
            )
    # todo should be coherent as stars??? or just a number is enough
    # if we think from the code perspective, not only the user perspective
    rating = models.IntegerField(choices=RATING_OPTIONS)

    def __str__(self):
        return self.rating
