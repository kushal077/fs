from django.contrib import admin
from django.urls import path ,include
from restro.views import homepage , menu  , restro , AmericanCuisines , MexicanCuisines ,ChineseCuisines , IndianCuisines , DesertCuisines
from . import views
from django.conf.urls import  url
from .models import Menu

urlpatterns = [
    path('',views.homepage,name="homepage"), # homepage=restro's
    path('restro/',views.restro,name="restros") ,# all restaurants.
    #path('restro/menu/',views.Menu,name="menu") ,# menu page
               path('acuisines/',views.AmericanCuisines), #american cuisines
               path('tcuisines/',views.ThaiCuisines), #thai cuisines
               path('mcuisines/',views.MexicanCuisines), # mexican cuisines
               path('ccuisines/',views.ChineseCuisines), # chinese cuisines
               path('icuisines/',views.IndianCuisines), # indian cuisines
               path('dcuisines/',views.DesertCuisines), #desert cuisines
    path('search/',views.search,name="search") , # search restro's
    url(r'^restro/(?P<id>[0-9]+)/menu/$',views.menu,name='menu'), #restro's menu
               
               #url(r'^cart/$',views.cart), # cart
    path('',include('django.contrib.auth.urls')), #auth for login
               ]

