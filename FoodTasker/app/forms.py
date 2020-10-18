from django import forms
from django.contrib.auth.models import User
 

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=("username","password","first_name","last_name","email")

class UserFormEdit(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=False)
    class Meta:
        model=User
        fields=("first_name","last_name","email")



