from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from workwithus.models import Signupclass 
from django.contrib.auth.models import User
from datetime import datetime
# import required module
import requests
import json

# Create your models here.
class Rescueclass(models.Model):
    #rid=models.IntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    animal=models.CharField(max_length=10)
    img= models.ImageField(null=True, blank=True,upload_to='images/')
    strt=models.CharField(max_length=30, default="None")
    lama=models.CharField(max_length=30, default="None")
    city=models.CharField(max_length=30, default="None")
    state=models.CharField(max_length=30, default="None")
    pin=models.CharField(max_length=30, default="None")
    def _str_(self):
        return self.name
    def save(self, *agrs, **kwargs):
        persons=Signupclass.objects.filter(pin=self.pin)
    
        for per in persons:
            

            url = " https://www.fast2sms.com/dev/bulkV2"
  
  
            payload = {"sender_id": "TXTIND",
            "message":f'There is a {self.animal} in need of rescue at :- {self.lama},{self.strt},{self.city}-{self.pin}     Help-seeker: {self.name} , {self.mobile}  Please Accept/Decline',
            "route": "v3",
            "numbers":f'{per.mobile}',
            }
            # create a dictionary
            headers = {
            'authorization': 'jgqkJFAQPMy9V50z3xiwbSKluYUGZftCo2BceLEN1rX4a6p87vCTPFKD0XiGqIU7JzB3AWhvoeH5jbm9',
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache"
             }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
         
        return super().save(*agrs,**kwargs)

class Message(models.Model):
    user=ForeignKey(User, on_delete=models.CASCADE)
    msg=CharField(max_length=500, default="None")
    dt=models.DateTimeField(default=datetime.now)