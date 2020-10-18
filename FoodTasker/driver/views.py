from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Sum, Count, Case, When

from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Driver

@login_required(login_url='/login') 
def driver_list(request):
     drivers = Driver.objects.annotate(total_order=Count(
          Case(When(order__restaurant=request.user.restaurant,
                    then=1)))).order_by("-total_order")

     all_drivers = [driver for driver in drivers if driver.total_order > 0]
     template_name = 'driver/driver_list.html'
     return render(request,template_name, {"all_drivers": all_drivers})

 