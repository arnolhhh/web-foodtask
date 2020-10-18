from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy  
from django.contrib.auth.decorators import login_required

from app.forms import UserForm,UserFormEdit
from .forms import RestaurantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from driver.models import Driver
from customer.models import Customer
from order.models import Order
from meal.models import Meal
from django.db.models import Sum, Count, Case, When

 
  
#@login_required(login_url='/login')
def Signup(request):
     user_form = UserForm()
     restaurant_form = RestaurantForm()
     template_name = 'restaurant/signup.html'

     if request.method=="POST":
          user_form=UserForm(request.POST)
          restaurant_form=RestaurantForm(request.POST,request.FILES)

          if user_form.is_valid() and restaurant_form.is_valid():
               new_user = User.objects.create_user(**user_form.cleaned_data)
               new_restaurant = restaurant_form.save(commit = False)
               new_restaurant.user = new_user
               new_restaurant.save()

               login(request, authenticate(
                    username = user_form.cleaned_data["username"],
                    password = user_form.cleaned_data["password"],
               ))

               return redirect(reverse_lazy('restaurant:restaurant-orders'))
               
     return render(request,template_name,{
          'user_form':user_form,
          'restaurant_form':restaurant_form
     })


def Orders(request):
     template_name = 'restaurant/orders.html'
     return render(request,template_name) 

def Account(request):     
     user_form = UserFormEdit(instance = request.user)
     restaurant_form = RestaurantForm(instance = request.user.restaurant)
     template_name = 'restaurant/account.html'

     if request.method=="POST":
          user_form=UserFormEdit(request.POST,instance = request.user)
          restaurant_form=RestaurantForm(request.POST,request.FILES,instance = request.user.restaurant)

          if user_form.is_valid() and restaurant_form.is_valid():              
               user_form.save()
               restaurant_form.save()

     return render(request,template_name,{
          'user_form':user_form,
          'restaurant_form':restaurant_form
     })


@login_required(login_url='/login')
def restaurant_report(request):
    return render(request, 'restaurant/reports.html', {})


@login_required(login_url='/login')
def restaurant_report(request):
    # Calculate revenue and number of order by current week
    from datetime import datetime, timedelta

    revenue = []
    orders = []

    # Calculate weekdays
    today = datetime.now()
    current_weekdays = [
        today + timedelta(days=i)
        for i in range(0 - today.weekday(), 7 - today.weekday())
    ]

    for day in current_weekdays:
        delivered_orders = Order.objects.filter(
            restaurant=request.user.restaurant,
            status=Order.DELIVERED,
            created_at__year=day.year,
            created_at__month=day.month,
            created_at__day=day.day)
        revenue.append(sum(order.total for order in delivered_orders))
        orders.append(delivered_orders.count())

    # Top 3 Meals
    top3_meals = Meal.objects.filter(restaurant = request.user.restaurant)\
                     .annotate(total_order = Sum('orderdetail__quantity'))\
                     .order_by("-total_order")[:3]

    meal = {
        "labels": [meal.name for meal in top3_meals],
        "data": [meal.total_order or 0 for meal in top3_meals]
    }

    # Top 3 Drivers
    top3_drivers = Driver.objects.annotate(total_order=Count(
        Case(When(order__restaurant=request.user.restaurant,
                  then=1)))).order_by("-total_order")[:3]

    driver = {
        "labels": [driver.user.get_full_name() for driver in top3_drivers],
        "data": [driver.total_order for driver in top3_drivers]
    }

    # Top 3 Drivers
    top3_customers = Customer.objects.annotate(total_order=Count(
        Case(When(order__restaurant=request.user.restaurant,
                  then=1)))).order_by("-total_order")[:3]

    customer = {
        "labels":
        [customer.user.get_full_name() for customer in top3_customers],
        "data": [customer.total_order for customer in top3_customers]
    }

    return render(
        request, 'restaurant/reports.html', {
            "revenue": revenue,
            "orders": orders,
            "meal": meal,
            "driver": driver,
            "customer": customer
        })


   

 