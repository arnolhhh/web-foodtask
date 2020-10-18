from django.urls import path
from django.contrib.auth import views as auth_views

from app.views import Home

urlpatterns = [
    path('',Home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='app/login.html'),name='logout'),
     
    #path('sin_privilegios/',HomeSinPrivilegios.as_view(),name='sin_privilegios')
]