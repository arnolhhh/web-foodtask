from django.urls import path 
from customer.views import customer_list

urlpatterns = [
    path('',customer_list,name='customer-list'),        
]