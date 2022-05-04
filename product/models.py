from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField()
    long_description = models.TextField()
    condition = models.CharField()
    featured_image = models.ImageField(upload_to='Images')

    def __str__(self):
        return self.name