# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#cuisines table
class cuisines(models.Model):
    cuisine=models.CharField(max_length=30)

    def __str__(self):
        return self.cuisine

#restaurant table
class Restaurant(models.Model):
    id = models.AutoField(max_length=20,blank=False,unique=True,primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    location_Address = models.TextField()
    image_url= models.CharField(max_length=300,blank=False,null=True)
    REST_STATE_CLOSED = "Closed"
    REST_STATE_OPEN = "Open"
    
    REST_STATE_CHOICES = (
                          (REST_STATE_OPEN,REST_STATE_OPEN),
                          (REST_STATE_CLOSED,REST_STATE_CLOSED)
                          )
        
    cuisines=models.ManyToManyField(cuisines)
    status=models.CharField(max_length=50,choices=REST_STATE_CHOICES,default=REST_STATE_OPEN)
    approved = models.BooleanField(blank=False,default=False)
                          
                          
    def __str__(self):
        return self.name

#food items table
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    food_choices=(
        ('snacks','snacks'),
        ('starter-veg','starter-veg'),
        ('starter-nonveg','starter-nonveg'),
        ('veg-maincourse','veg-maincourse'),
        ('nonveg-maincourse','nonveg-maincourse'),
        ('Breads','Breads'),
        ('Desert','Deserts'),
            )
    category = models.CharField(max_length=50,choices=food_choices)
    
    def __str__(self):
        return  self.name

#restro menu table
class Menu(models.Model):
    id = models.AutoField(blank=False,unique=True,primary_key=True)
    item_id = models.ForeignKey(Item  , on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    
    price = models.IntegerField(blank=False)
    image_url=models.CharField(max_length=300,blank=False,null=True)
    def __str__(self):
        return self.item_id.name+' - '+str(self.price)

      
'''
#order table
class Order(models.Model):
    id = models.IntegerField(blank=False)
    id = models.AutoField(primary_key=True)
    total_amount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_addr = models.CharField(max_length=50,blank=True)
    orderedby = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ORDER_STATE_WAITING = "Waiting"
    ORDER_STATE_PLACED = "Placed"
    ORDER_STATE_ACKNOWLEDGED = "Acknowledged"
    ORDER_STATE_COMPLETED = "Completed"
    ORDER_STATE_CANCELLED = "Cancelled"
    ORDER_STATE_DISPATCHED = "Dispatched"
    
    ORDER_STATE_CHOICES = (
                           (ORDER_STATE_WAITING,ORDER_STATE_WAITING),
                           (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
                           (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
                           (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
                           (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
                           (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
                           )
    status = models.CharField(max_length=50,choices=ORDER_STATE_CHOICES,default=ORDER_STATE_WAITING)
                           
    def __str__(self):
        return str(self.id)+' '+self.status
#item order table
class OrderItems(models.Model):
    #id = models.IntegerField(blank=False)
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    oid = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    
    def __unicode__(self):
        return str(self.id)
'''

#addtocart table
class ADDCART(models.Model):
    i=models.AutoField(primary_key=True)
    id=models.CharField(max_length=20,blank=False)
    price=models.IntegerField(blank=False)
    image=models.CharField(max_length=300,blank=False,null=True)
    def __unicode__(self):
        return self.id
