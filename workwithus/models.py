from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signupclass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    strt=models.CharField(max_length=30, default="None")
    lama=models.CharField(max_length=30, default="None")
    city=models.CharField(max_length=30, default="None")
    state=models.CharField(max_length=30, default="None")
    pin=models.CharField(max_length=30, default="None")

