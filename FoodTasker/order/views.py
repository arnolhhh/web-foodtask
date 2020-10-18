from django.shortcuts import render,redirect 
from django.urls import reverse_lazy  

from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm

@login_required(login_url='/login') 
def order_create(request):
     template_name = 'order/order_form.html'
     form = OrderForm()     

     if request.method=="POST":           
          form=OrderForm(request.POST,request.FILES)

          if form.is_valid():                
               order = form.save(commit = False)
               order.restaurant = request.user.restaurant
               order.save()

               return redirect(reverse_lazy('order:order-list'))
               
     return render(request,template_name,{
          'form':form,         
     }) 

@login_required(login_url='/login') 
def order_edit(request,id):
     template_name = 'order/order_form.html'
     form = OrderForm(instance = order.objects.get(id=id))     

     if request.method=="POST":           
          form=OrderForm(request.POST,request.FILES,instance = Order.objects.get(id=id))

          if form.is_valid():                
               form.save()
               return redirect(reverse_lazy('order:order-list'))
               
     return render(request,template_name,{
          'form':form,         
     }) 
      

@login_required(login_url='/login') 
def order_list(request):
    template_name = 'order/order_list.html'
     #orders = order.objects.all()
    if request.method=="POST":           
        order=Order.objects.get(id=request.POST['id'],restaurant=request.user.restaurant)

        if order.status==Order.COOKING:
            order.status= Order.READY               
            order.save()

    orders=Order.objects.filter(restaurant=request.user.restaurant).order_by('-id')

    return render(request,template_name,{
        'orders':orders,         
    }) 
