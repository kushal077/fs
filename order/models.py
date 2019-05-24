from django.db import models
from restro.models import cart
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save , post_save
from restro.models import cart
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
status=(
        ('order accepted', 'order accepted' ),
        ('order declined' ,'order declined' ),
)



# Create your models here.
class Order(models.Model):
    order_id=models.CharField(max_length=20,blank=True,unique=True)
    cart= models.ForeignKey(cart,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default="order accepted", choices=status)
    total=models.DecimalField(default=0.0,max_digits=100,decimal_places=2)
    #billing=models.ForeignKey(OrderPlaced,on_delete=models.CASCADE)
    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total= self.cart.total
        self.total=cart_total
        self.save()
        return cart_total

def pre_save_create_order_id(sender, instance, *args , **kwargs):
    if not instance.order_id:
        instance.order_id= unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender= Order)

def post_save_cart_total(sender, instance , created, *args , **kwargs):
    if not created:
        cart_obj=instance
        cart_total=cart_obj.total
        cart_id= cart_obj.id
        qs= Order.objects.filter(cart__id= cart_id)
        if qs.count()==1:
            order_obj=qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total , sender=cart)

def post_save_order(sender , instance ,created , *args , **kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order, sender=Order)

#order placed= billing !
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #order_id= models.ForeignKey(Order,on_delete=models.CASCADE)
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    country_city= models.CharField(max_length=10,default="INDIA- Delhi NCR")
    email=models.EmailField(max_length=50,blank=False)
    fullname=models.CharField(max_length=100,blank=False)
    street_address= models.CharField(max_length=150,blank=False)
    pin=models.CharField(max_length=10,blank=False)
    payment= models.CharField(max_length=100,default="COD")

    def __str__(self):
        return self.email

