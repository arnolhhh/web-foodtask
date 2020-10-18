from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from .forms import UserForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.views import generic

@login_required(login_url='/login')
def Home(request):
    template_name = 'app/home.html'
    return render(request,template_name)
   
 
 