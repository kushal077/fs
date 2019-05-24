"""foodsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path ,include
#from restro.views import addtocart
from restro import views
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns
from order.views import order_placed , handlerequest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restro.urls')),
    path('',include( 'accounts.urls')),
    path('',include('django.contrib.auth.urls')), #auth for login
    path('placed/',order_placed),
    path("handlerequest/", handlerequest , name="HandleRequest"),
               ]

urlpatterns += staticfiles_urlpatterns()

