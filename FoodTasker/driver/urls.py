from django.urls import path 
from driver.views import driver_list

urlpatterns = [
    path('',driver_list,name='driver-list'),        
]