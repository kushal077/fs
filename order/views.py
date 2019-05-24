from django.shortcuts import render
from django.http import HttpResponse
from order.models import OrderPlaced
# Create your views here.

from .payTm import Checksum
from django.views.decorators.csrf import csrf_exempt

def order_placed(request):
    if request.method=="POST":
        email=request.POST['Email']
        name=request.POST.get('Name',False)
        Address=request.POST['Address']
        pin= request.POST['pin']

        OrderPlaced.objects.create(
                    user=request.user,
                    email=email,
                    fullname=name,
                    street_address= Address,
                    pin=pin,
                                 )

    #request paytm to transfer the amount to your account after payment by user!
        param_dict = {
            'MID': 'zllHED46628055305623',
            #'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'restro/paytm.html', {'param_dict': param_dict})
            #return render(request, 'shop/checkout.html')


    return render(render,'restro/checkout.html')

@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here!
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, '/paymentstatus.html', {'response': response_dict})



