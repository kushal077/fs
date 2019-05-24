# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save , post_save ,m2m_changed


#restaurant table
class Restaurant(models.Model):
    id = models.AutoField(max_length=20,blank=False,unique=True,primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    location_Address = models.TextField()
    image_url= models.CharField(max_length=300,blank=False,null=True)
    REST_STATE_CLOSED = "Closed"
    REST_STATE_OPEN = "Open"
    cuisine_choices=(
                     ('American','american'),
                     ('Thai','thai'),
                     ('Mexican','mexican'),
                     ('chinese','Chinese'),
                     ('indian','indian'),
                     ('Desert','Desert')
                     )
                    
    
    
    REST_STATE_CHOICES = (
                          (REST_STATE_OPEN,REST_STATE_OPEN),
                          (REST_STATE_CLOSED,REST_STATE_CLOSED)
                          )
        
    cuisines1=models.CharField(max_length=10,choices=cuisine_choices)
    cuisines2=models.CharField(max_length=10,blank=True,null=False,choices=cuisine_choices)

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
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    #slug=models.SlugField(blank=True,unique=True)
    restaurant_id = models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)
    image_url=models.CharField(max_length=300,blank=False,null=True)

    def __str__(self):
        return 'food : {} {}, Restro: {}'.format(self.item_id.name , self.price, self.restaurant_id.name)


        #    def menu_pre_save_receiver(sender , instance , *args , **kwargs):
        # if not instance.slug:
        #   instance.slug= unique_slug_generator(instance)
        #   pre_save.connect(menu_pre_save_receiver, sender= Menu)


        #def get_absolute_url(self):
#return reverse("menu:detail",kwargs={"slug":self.slug})

#def __str__(self):
#return self.item_id.name+' - '+str(self.price)


class CartManager(models.Manager):
    def new_or_get(self,request):
        cart_id= request.session.get('cart_id', None)
        qs=cart.objects.filter(id=cart_id)
        if qs.count()==1:
            new_obj=False
            cart_obj=qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user=request.user
                cart_obj.save()
        else:
            cart_obj=cart.objects.new(user=request.user)
            new_obj=True
            request.session['cart_id']=cart_obj.id
        return cart_obj , new_obj
    
    def new(self,user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
        return self.model.objects.create(user=user_obj)

class cart(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    product=models.ManyToManyField(Menu,blank=True)
    total=models.DecimalField(default=0.0,max_digits=100,decimal_places=2)
    updated=models.DateTimeField(auto_now=True)
    
    objects= CartManager()
    
    
    
    def __str__(self):
        return str(self.id)


def pre_save_cart_receiver(sender, instance, action , *args , **kwargs):
    #print(action)
    
    products= instance.product.all()
    total=0
    for x in products:
        total+= x.price
    if total <=300:
        instance.total= total + 30
        instance.save()
    elif total > 300:
        instance.total= total 
        instance.save()


m2m_changed.connect(pre_save_cart_receiver, sender=cart.product.through)















