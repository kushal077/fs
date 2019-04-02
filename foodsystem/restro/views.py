from django.shortcuts import render ,redirect
from restro.models import Restaurant , Menu , ADDCART
from django.views.generic import ListView ,DetailView
#from django.urls import reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
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
'''
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
'''

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
'''
class homepage(ListView):
    model=Restaurant
    #query=request.GET.get("q")
    queryset=Restaurant.objects.filter(title_icontains=q)
        #  query=request.GET.get("q")
        # if query:
        #queryset_list=queryset_list.filter(title_icontains=query)
'''
# 1:homepage
def homepage(request):
    return render(request,'restro/restrobase.html')

# 2:restropage
def restro(request):
    r=Restaurant.objects.all()
    restro={'r':r,'r_count':len(r)}
    return render(request,'restro/restros.html',restro)

#3:menu
def menu(request,id):
    re=Menu.objects.filter(restaurant_id=id)
    restro={'r':re}
    return render(request,'restro/menus.html',restro)

#4: search
def search(request):
    if request.method=='POST':
        src=request.POST['search']
        if src:
            match=Restaurant.objects.filter(Q(name__icontains=src))
            
            if match:
                return render(request,'restro/search.html' ,{'sr':match})
            else:
                messages.error(request,'no restaurant find!')
        else:
            return HttpResponseRediract('/search/')

    return render(request,'restro/search.html')

#5 choosecuisines
def AmericanCuisines(request):
    Cuisine=Restaurant.objects.filter(Q(cuisines1="American") |  Q(cuisines2="American"))
    restro={'r':Cuisine}
    return render(request,'restro/cuisines.html',restro)

def ThaiCuisines(request):
    Cuisine=Restaurant.objects.filter(Q(cuisines1="Thai") |  Q(cuisines2="Thai"))
    restro={'r':Cuisine}
    return render(request,'restro/cuisines.html',restro)

def MexicanCuisines(request):
    Cuisine=Restaurant.objects.filter(Q(cuisines1="Mexican") |  Q(cuisines2="Mexican"))
    restro={'r':Cuisine}
    return render(request,'restro/cuisines.html',restro)

def ChineseCuisines(request):
    Cuisine=Restaurant.objects.filter(Q(cuisines1="chinese") |  Q(cuisines2="chinese"))
    restro={'r':Cuisine}
    return render(request,'restro/cuisines.html',restro)

def IndianCuisines(request):
    Cuisine=Restaurant.objects.filter(Q(cuisines1="Indian") |  Q(cuisines2="Indian"))
    restro={'r':Cuisine}
    return render(request,'restro/cuisines.html',restro)

def DesertCuisines(request):
    Cuisine=Restaurant.objects.filter(Q(cuisines1="Desert") |  Q(cuisines2="Desert"))
    restro={'r':Cuisine}
    return render(request,'restro/cuisines.html',restro)

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
