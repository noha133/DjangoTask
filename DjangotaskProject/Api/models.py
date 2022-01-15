from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    seller = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return str(self.name)