from django.urls import path 
from .views import order_list,order_create,order_edit

urlpatterns = [
    path('',order_list,name='order-list'),
    path('create',order_create,name='order-create'),
    path('edit/<int:id>',order_edit, name="order-edit"),
]