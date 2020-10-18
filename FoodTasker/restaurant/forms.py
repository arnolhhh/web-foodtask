from django import forms
from django.contrib.auth.models import User
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=("name","phone","address","logo")