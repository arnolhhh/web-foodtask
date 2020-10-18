from django.urls import path 
from .views import meal_list,meal_create,meal_edit

urlpatterns = [
    path('',meal_list,name='meal-list'),
    path('create',meal_create,name='meal-create'),
    path('edit/<int:id>',meal_edit, name="meal-edit"),
]