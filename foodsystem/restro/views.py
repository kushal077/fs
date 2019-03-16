from django.shortcuts import render ,redirect
from restro.models import Restaurant , Menu , ADDCART
from django.views.generic import ListView ,DetailView
#from django.urls import reverse
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_protect

#from django.views.generic import ListView
# Create your views here.
'''
    # function based view
def homepage(request):
    restro=Restaurant.objects.all()
    res={'restro':restro}
    return render(request,'restro/restro.html',res)
'''

def cartItem(cart):
    items=[]
    for item in cart:
        items.append(Menu.objects.get(id=item))
    return items

def menu(request,id):
    cart=[]
    if'cart' not in request.session:
        request.session['cart']=[]
    cart=request.session['cart']
    request.session.set_expiry(0)
    men=Menu.objects.filter(restaurant_id=id)
    ctx={'menu':men, 'cart_size':len(cart)}

    if request.method=="POST":
        cart.append(int(request.POST['obj_id']))
        return redirect(menu,id)

    return render(request,'restro/menu.html',ctx)

def cart(request):
    cart= request.session['cart']
    request.session.set_expiry(0)
    Ctx={'cart':cart , 'cart size':len(cart) , 'cart_items' :cartItem(cart) ,'total_price': pricecart(cart) }
    return render(request ,'restro/cart.html', Ctx)

def pricecart(cart):
    cart_items=cartItem(cart)
    price=0
    for item in cart_items:
        price += item.price
    return price

#generic class based vie
class homepage(ListView):
    model=Restaurant

'''
def removefromcart(request):
    request.session.set_expiry(0)
    obj_to_remove=int(request.post['obj_id'])
    obj_index=request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(obj_index)
    return redirect('cart')
'''
@csrf_protect
def addtocart(request):
    if request.method=="POST":
        name=request.POST['rname']
        price=request.POST['rprice']
        image=request.POST['rimage']

        ADDCART.objects.create(
            id=name,
            price=price,
            image=image,
                )
    return HttpResponse('')
