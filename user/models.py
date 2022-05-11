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
    bio = models.CharField(max_length=999, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999, default='https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png')
    # status_log = models.BooleanField(default=False)

    def __str__(self):
        return self.name
