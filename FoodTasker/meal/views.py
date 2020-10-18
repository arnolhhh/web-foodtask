from django.shortcuts import render,redirect 
from django.urls import reverse_lazy  

from django.contrib.auth.decorators import login_required
from .models import Meal
from .forms import MealForm

@login_required(login_url='/login') 
def meal_create(request):
     template_name = 'meal/meal_form.html'
     form = MealForm()     

     if request.method=="POST":           
          form=MealForm(request.POST,request.FILES)

          if form.is_valid():                
               meal = form.save(commit = False)
               meal.restaurant = request.user.restaurant
               meal.save()

               return redirect(reverse_lazy('meal:meal-list'))
               
     return render(request,template_name,{
          'form':form,         
     }) 

@login_required(login_url='/login') 
def meal_edit(request,id):
     template_name = 'meal/meal_form.html'
     form = MealForm(instance = Meal.objects.get(id=id))     

     if request.method=="POST":           
          form=MealForm(request.POST,request.FILES,instance = Meal.objects.get(id=id))

          if form.is_valid():                
               form.save()
               return redirect(reverse_lazy('meal:meal-list'))
               
     return render(request,template_name,{
          'form':form,         
     }) 

@login_required(login_url='/login') 
def meal_list(request):
     template_name = 'meal/meal_list.html'
     #meals = Meal.objects.all()
     meals=Meal.objects.filter(restaurant=request.user.restaurant).order_by('-id')
     return render(request,template_name,{
          'meals':meals,         
     }) 
