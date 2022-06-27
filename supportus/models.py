from django.db import models

# Create your models here.
class Donateclass(models.Model):
    #did=models.IntegerField(primary_key=True,default=1,unique=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=10)
    comment=models.CharField(max_length=50)
    add=models.CharField(max_length=100, default="None")
    #state=models.CharField(max_length=15)
    anony=models.CharField(max_length=5,default="No")
    amt=models.IntegerField(default=0)
'''
def savedonate(self, *args, **kwargs):
    self.did= self.did + 1
    super().save(*args, **kwargs)
'''
