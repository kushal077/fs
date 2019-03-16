from django.contrib import admin
from django.urls import path ,include
from restro.views import homepage , menu  
from . import views
from django.conf.urls import  url
from .models import Menu

urlpatterns = [
    path('',homepage.as_view(template_name='restro/restro.html')), # homepage=restro's
    url(r'^(?P<id>[0-9]+)/menu/$',views.menu,name='restromenu'), #restro's menu
               
    url(r'^cart/$',views.cart), # cart
    path('',include('django.contrib.auth.urls')), #auth for login
               ]

