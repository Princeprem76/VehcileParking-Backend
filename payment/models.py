from django.db import models
from parkingspace.models import Parking

from user.models import User

# Create your models here.

class Payments(models.Model):
    # select = [('E-payment', 'E-payment'), ('Cash', 'Cash')]
    price = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Parking, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    payment_done = models.BooleanField()


class notify(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
