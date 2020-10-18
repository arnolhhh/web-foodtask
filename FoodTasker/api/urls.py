from django.urls import path, include
from . import views

urlpatterns = [
    # APIs for RESTAURANT    
    path('order/notification/<str:last_request_time>',views.restaurant_order_notification), 
    
    # APIs for CUSTOMER
    path('customer/restaurants/',views.customer_get_restaurant),
    path('customer/meals/<int:restaurant_id>',views.customer_get_meals),      
    path('customer/order/add',views.customer_add_order), 
    path('customer/order/latest',views.customer_get_latest_order),    
    path('customer/driver/location',views.customer_driver_location), 
    path('customer/order/history', views.customer_get_order_history),


    # APIs for DRIVERS
    path('driver/orders/ready', views.driver_get_ready_orders),
    path('driver/order/pick', views.driver_pick_order),
    path('driver/order/latest', views.driver_get_latest_order),
    path('driver/order/complete', views.driver_complete_order),
    path('driver/revenue', views.driver_get_revenue),
    path('driver/location/update', views.driver_update_location),
    path('driver/order/history', views.driver_get_order_history),

]