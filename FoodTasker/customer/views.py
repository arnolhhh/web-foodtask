from django.shortcuts import render 
from django.db.models import Sum, Count, Case, When

from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Customer

@login_required(login_url='/login') 
def customer_list(request):     
    customers = Customer.objects.annotate(total_order=Count(
        Case(When(order__restaurant=request.user.restaurant,
                  then=1)))).order_by("-total_order")

    all_customers = [
        customer for customer in customers if customer.total_order > 0
    ]

    return render(request, 'customer/customer_list.html',
                  {"all_customers": all_customers})


 

   

 