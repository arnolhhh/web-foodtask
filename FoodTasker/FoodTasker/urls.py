"""FoodTasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('',include(('app.urls','app'), namespace='app')),
    path('api/',include(('api.urls','api'), namespace='api')),
    path('customer/',include(('customer.urls','customer'), namespace='customer')),
    path('driver/',include(('driver.urls','driver'), namespace='driver')),
    path('meal/',include(('meal.urls','meal'), namespace='meal')),
    path('order/',include(('order.urls','order'), namespace='order')),
    path('restaurant/',include(('restaurant.urls','restaurant'), namespace='restaurant')),    
    path('admin/', admin.site.urls),    
    path('auth/', include('rest_framework_social_oauth2.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)