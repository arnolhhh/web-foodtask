from django.urls import path
 
from .views import Signup,Account,Orders,restaurant_report

urlpatterns = [
    path('register',Signup,name='restaurant-register'),
    path('orders',Orders,name='restaurant-orders'), 
    path('account',Account,name='restaurant-account'),
    path('reports',restaurant_report,name='restaurant-reports'),
]