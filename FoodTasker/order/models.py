from django.db import models
from customer.models import Customer
from restaurant.models import Restaurant
from driver.models import Driver
from meal.models import Meal

class Order(models.Model): 
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICES=(
        (COOKING,'Cooking'),
        (READY,'Ready'),
        (ONTHEWAY,'On The Way'),
        (DELIVERED,'Delivered'),
    )

    customer= models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='order')   
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='order') 
    driver= models.ForeignKey(Driver, on_delete=models.CASCADE,related_name='order')
    address=models.CharField(max_length=500)
    total=models.IntegerField(default=0)
    status=models.IntegerField(choices = STATUS_CHOICES,null=True) 
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    picked_at=models.DateTimeField(blank=True,null=True)
     
    def __str__(self):
        return str(self.id)

class OrderDetail(models.Model): 
    order= models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_details') 
    meal= models.ForeignKey(Meal,on_delete=models.CASCADE)    
    quantity=models.IntegerField(default=0)
    sub_total=models.IntegerField(default=0)
     
    def __str__(self):
        return str(self.id)