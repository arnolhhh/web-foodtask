from django.db import models
from restaurant.models import Restaurant

class Meal(models.Model): 
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='meal')   
    name=models.CharField(max_length=500)
    short_description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='meal_images/', blank=False)
    price=models.IntegerField(default=0)
     
    def __str__(self):
        return self.name