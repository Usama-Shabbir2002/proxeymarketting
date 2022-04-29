from django.shortcuts import render
from PMM.models import Order
from PMM.models import Product
from PMM.models import Pmmreservation
from PMM.models import Commission
from PMM.models import Pmm
from PMM.models import Pm
from datetime import datetime
from datetime import timedelta


# Create your views here.

# done done done done done done done
def homepage(request):
    # if(PMM != 'PMM' and PM != 'PM' and Admin != 'Admin'):
    PMM = request.GET.get('user','off')
    print(PMM)
    if PMM == 'PMM':
        return render(request, 'homepage.html')
    PM = request.GET.get('user','off')
    if PM == 'PM':
        return render(request, 'homepagePM.html')
    Admin = request.GET.get('user','off')
    if Admin == 'Admin':
        return render(request, 'homepageAdmin.html')
def homepagePMM(request):
    return render(request, 'homepage.html')
def products(request):
    # if request.method == 'GET':
        pid = request.GET.get('Pid')
        #print(pid)
        pkw = request.GET.get('Pkw')
        # print(pkw)
        market = request.GET.get('Market')
        # print(market)
        ptype = request.GET.get('Type')
        # print(ptype)
        products = Product.objects.all()
        if (pkw != '' and pkw is not None) and (market != '' and market is not None) and (ptype != '' and ptype is not None) and (pid != '' and pid is not None)  :
            products = Product.objects.filter(keyword=pkw , country=market , type= ptype, id=pid)
        elif (pkw != '' and pkw is not None) and (market != '' and market is not None) and (ptype != '' and ptype is not None) :
            products = Product.objects.filter(keyword=pkw , country=market , type= ptype)
        elif (pkw != '' and pkw is not None) and (market != '' and market is not None) and (pid != '' and pid is not None) :
            products = Product.objects.filter(keyword=pkw , country=market , id= pid)
        elif (pid != '' and pid is not None) and (market != '' and market is not None) and (ptype != '' and ptype is not None) :
            products = Product.objects.filter(id=pid , country=market , type= ptype)
        elif (pkw != '' and pkw is not None) and (pid != '' and pid is not None) and (ptype != '' and ptype is not None) :
            products = Product.objects.filter(keyword=pkw , id=pid , type= ptype)

        elif (market != '' and market is not None) and (ptype != '' and ptype is not None) :
            products = Product.objects.filter(country=market , type= ptype)
        elif (pkw != '' and pkw is not None) and (ptype != '' and ptype is not None) :
            products = Product.objects.filter(keyword=pkw  , type= ptype)
        elif (pkw != '' and pkw is not None) and (market != '' and market is not None) :
            products = Product.objects.filter(keyword=pkw , country=market )
        
        elif (pkw != '' and pkw is not None)  :
            products = Product.objects.filter(keyword=pkw )
        elif  (market != '' and market is not None)  :
            products = Product.objects.filter( country=market )
        elif (ptype != '' and ptype is not None) :
            products = Product.objects.filter( type= ptype)
        elif (pid != '' and pid is not None) :
            products = Product.objects.filter( id= pid)
    # products= Product.objects.raw("select * from PMM_Product where country='USA' and id = 1 ")
    
        context = {
            'products' : products}
        # print(context)
        if request.method == 'GET':

            return render(request, 'products.html',context)

        if request.method == 'POST':
            # print(pkw)
            reservations = Product.objects.filter(id=pid)
            context = {
            'reservations' : reservations}
            print(context)
            for items in reservations:
                pid = items.id
                pkw= items.keyword
                brand= items.brand
                Store= items.store
                commission= items.commissionn
                type= items.type
                country= items. country
                image= items.image
                current_time = datetime.now()
                Pmmreservation( time= current_time, keywordd=pkw, rid= pid,  brand=brand, store=Store, commissionn=commission, type=type, country=country, image=image).save()
            print(image)
            return render(request, 'Reservation.html', context)
            print('hello')
def Orders(request):
    orders = Order.objects.all()
    ono = request.GET.get('orderno')
    print(ono)
    Oppal = request.GET.get('paypal')
    otype = request.GET.get('Type')
    
    if (Oppal != '' and Oppal is not None) and (otype != '' and otype is not None) and (ono != '' and ono is not None) :
            orders = Order.objects.filter(paypal=Oppal , status= otype, orderno= ono)
    elif (Oppal != '' and Oppal is not None) and (otype != '' and otype is not None) :
            orders = Order.objects.filter(paypal=Oppal, status= otype)
    elif (Oppal != '' and Oppal is not None) and (ono != '' and ono is not None) :
            orders = Order.objects.filter(paypal=Oppal, orderno= ono)
    elif (ono != '' and ono is not None) and (otype != '' and otype is not None) :
            orders = Order.objects.filter(orderno=ono, status= otype)
    elif (Oppal != '' and Oppal is not None) :
            orders = Order.objects.filter(paypal= Oppal)
    
    elif (otype != '' and otype is not None) :
            orders = Order.objects.filter(status= otype)
    elif (ono != '' and ono is not None) :
            orders = Order.objects.filter(orderno= ono)
    context = {
        'orders' : orders}
    # if request.method == 'POST':
     #   orders = Order.objects.filter(paypal=Oppal)
      #  context = {
       #     'orders' : orders}
       # print(context)
       # for items in orders:
        #    Order(orderno=orderno, paypal=paypal, Reviewimage=Rimage).save()
        
    return render(request, 'order.html', context)
def orderupdate(request):
    orders = Order.objects.all()
    ono = request.GET.get('Onumber')
    Oppal = request.GET.get('PayPal')
    print(Oppal)
    if (Oppal != '' and Oppal is not None) :
            orders = Order.objects.filter(paypal=Oppal)
    context = {
        'orders' : orders}
    # print(context)
    if request.method == 'POST':
        orders = Order.objects.filter(paypal=Oppal)
        context = {
        'orders' : orders}
        print(context)
        
        # if request.FILES["Rvscreenshot"] != '' and request.FILES["Rvscreenshot"] is not None:
        #  reviewimage = request.FILES["Rvscreenshot"]
        #else:
        #   reviewimage = 'NULL' 
        #print(reviewimage)
        for items in orders:
            orderimage = items.orderimage
        reviewimage = request.FILES["Rvscreenshot"]
        # print(reviewimage)
        status = 'Reviewed'
        Order(orderno=ono, paypal=Oppal, orderimage=orderimage,status=status, Reviewimage=reviewimage).save()

    return render(request, 'orderupdate.html',context)
def Profile(request):
    profile = Pmm.objects.all()
    context= {
        'profile' : profile
    }
    return render(request, 'User Profile.html', context)
def Commision(request):
    commission = Order.objects.filter(status='Refunded')
    context = {
        'commission' : commission}
    for items in commission:
        onumber = items.orderno
        ppal = items.paypal
        commision = 550
        date = datetime.now()
    # cmm = Commission.objects.raw("select * from Commission")
        cmm = Commission.objects.all()
        contextt = {
        'cmm' : cmm}
        #print(contextt)
        statuss= ''
        for itemss in cmm:
        # print('sambaa')
            print(itemss)
            if itemss.orderno != onumber:
                statuss= 'notexisted'
            if statuss == 'notexisted':
                Commission(orderno= onumber, paypal= ppal, commissionnn= commision, date= date).save()
    return render(request, 'Commision.html',context)
def Reservation(request):
    reservations = Pmmreservation.objects.all()
    pidd = request.GET.get('pidd')
    pkww = request.GET.get('pkww')
    if (pidd != '' and pidd is not None) and (pkww != '' and pkww is not None) :
            reservations = Pmmreservation.objects.filter(rid=pidd , keywordd= pkww)
    if (pidd != '' and pidd is not None) :
            reservations = Pmmreservation.objects.filter(rid=pidd)
    if (pkww != '' and pkww is not None) :
            reservations = Pmmreservation.objects.filter(keywordd= pkww)
    context = {
        'reservations' : reservations}
    
    return render(request, 'Reservation.html', context)
def deleresservation(request):
    reservations = Pmmreservation.objects.all().delete()
    context = {
        'reservations' : reservations}
    print(context)
    return render(request, 'Reservation.html')
def Rules(request):
    return render(request, 'Rules and Regulations.html')
def Orderform(request):
    if request.method == 'POST':
        orderno = request.POST.get('Onumber')
        status = request.POST.get('status')
        paypal = request.POST.get('PayPal')
        if request.FILES["Oscreenshot"] != '' and request.FILES["Oscreenshot"] is not None:
            orderimage = request.FILES["Oscreenshot"]
        # if request.FILES["Rscreenshot"] != '' and request.FILES["Rscreenshot"] is not None:
        #   reviewimage = request.FILES["Rscreenshot"]
        # else:
        #    reviewimage = 'NULL' 
        # if request.FILES["Rfscreenshot"] != '' and request.FILES["Rfscreenshot"] is not None:
        #    refundimage = request.FILES["Rfscreenshot"]
        # else:
        #    refundimage = 'NULL'

        Order(orderno=orderno, paypal=paypal, orderimage=orderimage, status = status).save()
        return render(request, 'Order Form.html')
    else:
        return render(request, 'Order Form.html')


# views for PM begins from Here
# done done done done done
def homepagePM(request):
    return render(request, 'homepagePM.html')
def productsPM(request):
    pid = request.GET.get('id')
    #print(pid)
    products= Product.objects.all()
    context = {
        'products': products
    } 
    if (pid != '' and pid is not None) :
            products = Product.objects.filter( id= pid)
            context = {
            'products': products
            }

    if request.method == 'POST':
        # print("qqq")
        products.delete()
    return render(request, 'productsPM.html', context)
def orderupdatepm(request):
    orders = Order.objects.all()
    ono = request.GET.get('Onumber')
    print(ono)
    # print(Oppal)
    if (ono != '' and ono is not None) :
            orders = Order.objects.filter(orderno=ono)
    context = {
        'orders' : orders}
    # print(context)
    if request.method == 'POST':
        orders = Order.objects.filter(orderno=ono)
        context = {
        'orders' : orders}
        print(context)
        
        # if request.FILES["Rvscreenshot"] != '' and request.FILES["Rvscreenshot"] is not None:
        #  reviewimage = request.FILES["Rvscreenshot"]
        #else:
        #   reviewimage = 'NULL' 
        #print(reviewimage)
        for items in orders:
            Oppal = items.paypal
            orderimage = items.orderimage
            reviewimage = items.Reviewimage
            refundimage = request.FILES["Rfscreenshot"]
        # print(reviewimage)
        status = 'Refunded'
        Order(orderno=ono, paypal=Oppal, Refundimage=refundimage, orderimage=orderimage,status=status, Reviewimage=reviewimage).save()

    return render(request, 'orderupdatepm.html',context)
def OrdersPM(request):
    oid = request.GET.get('id')
    #print(pid)
    orders= Order.objects.all()
    context = {
        'orders': orders
    } 
    if (oid != '' and oid is not None) :
            orders = Order.objects.filter( orderno= oid)
            context = {
            'orders': orders
            }

    if request.method == 'POST':
         print("qqq")
        #products.delete()
    return render(request, 'OrdersPM.html', context)
def CommisionPM(request):
    commission = Order.objects.filter(status='Refunded')
    context = {
        'commission' : commission}
    for items in commission:
        onumber = items.orderno
        ppal = items.paypal
        commision = 550
        date = datetime.now()
    # cmm = Commission.objects.raw("select * from Commission")
        cmm = Commission.objects.all()
        contextt = {
        'cmm' : cmm}
        #print(contextt)
        statuss= ''
        for itemss in cmm:
        # print('sambaa')
            print(itemss)
            if itemss.orderno != onumber:
                statuss= 'notexisted'
            if statuss == 'notexisted':
                Commission(orderno= onumber, paypal= ppal, commissionnn= commision, date= date).save()
    return render(request, 'CommissionPM.html',context)
def ReservationPM(request):
    return render(request, 'ReservationPM.html')
def ProfilePM(request):
    return render(request, 'UserProfilePM.html')
def productadd(request):
    if request.method == 'POST':
        #print("aaa")
        pkw = request.POST.get('Pkw')
        #print(pkw)
        market = request.POST.get('Market')
        #print(market)
        type = request.POST.get('Type')
        #print(type)
        brand = request.POST.get('brand')
        #print(brand)
        store = request.POST.get('store')
        #print(store)
        comm = request.POST.get('comm')
        #print(comm)
        total = request.POST.get('Quantity')
        #print(total)
        limit = request.POST.get('limit')
        #print(limit)
        cat = request.POST.get('Category')
        #print(cat)
        if (request.FILES["pimage"]) != '' or (request.FILES["pimage"]) is not None:
             img = request.FILES["pimage"]
        #print(img)
        Product(keyword=pkw, country=market, type=type, brand=brand, store=store, commissionn=comm, totalquantity=total, dailylimit=limit, image= img).save()

    return render(request, 'Product Form.html')


# views for Admins begins from Here
def homepageAdmin(request):
    return render(request, 'homepageAdmin.html')
def removePM(request):
    id = request.GET.get('pmid')
    
    pms = Pm.objects.filter(id=id).delete()
    print(pms)
    context={
        'pms' : pms
    }
    #print(context)
    return render(request, 'RemovePM.html', context)
def removePMM(request):
    id = request.GET.get('pmmid')
    pmms = Pmm.objects.filter(id=id).delete()
    print(pmms)
    context={
        'pmms' : pmms
    }
    return render(request, 'RemovePMM.html',context)
def deleteorder(request):
    onumber = request.GET.get('ono')
    Order.objects.filter(orderno=onumber).delete()
    return render(request, 'Deleteorder.html')