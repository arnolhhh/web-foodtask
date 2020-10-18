from django.db import models
from django.contrib.auth.models import User
  
class Driver(models.Model): 
    user= models.OneToOneField(User, on_delete=models.CASCADE,related_name='driver')   
    avatar=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
     
    def __str__(self):
        return self.user.get_full_name()     