from django.shortcuts import render,redirect
from guest.models import *
from Shop.models import *
from user.models import *
from administrator.models import *
from datetime import date
from django.db.models import Sum
# Create your views here.



def homepage(request):
    return render(request,"Shop/Homepage.html")

def my_pro(request):
    data=tbl_shop.objects.get(id=request.session["sid"])
    return render(request,"Shop/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        prodata.shop_name=request.POST.get('txtname')
        prodata.shop_contact=request.POST.get('txtcon')
        prodata.shop_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Shop/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Shop/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_shop.objects.filter(id=request.session["sid"],shop_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                sdata=tbl_shop.objects.get(id=request.session["sid"],shop_password=request.POST.get('txtcurpass'))
                sdata.shop_password=request.POST.get('txtnewpass')
                sdata.save()
                return render(request,"Shop/Changepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Shop/Changepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Shop/Changepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Shop/Changepassword.html")





def productinsertselect(request):
    data=tbl_product.objects.all()
    for product in data:
        total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_cart.objects.filter(product=product.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        print(total_stock,"stock")
        print(total_cart,"cart")
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        if isinstance(total_stock, int):
            total_stock = total_stock
        else:
            total_stock = 0     
            if isinstance(total_cart, int):
                total_cart = total_cart
            else:
                total_cart = 0
        total=  total_stock-total_cart
        product.total_stock = total
    cat = tbl_category.objects.all()
    brand = tbl_brand.objects.all()
    color = tbl_color.objects.all()
    if request.method=="POST":
        name=request.POST.get("txtname")
        det=request.POST.get("txtdetails")
        rate=request.POST.get("txtrate")
        photo=request.FILES.get("filephoto")
        shop=tbl_shop.objects.get(id=request.session["sid"])
        shand=request.objects.get("Second")
        subcategory = tbl_subcategory.objects.get(id=request.POST.get('sel_sub'))
        brand = tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        color = tbl_color.objects.get(id=request.POST.get('sel_color'))
        tbl_product.objects.create(product_name=name,product_rate=rate,product_details=det,product_photo=photo,shop=shop,brand=brand,color=color,subcategory=subcategory,second_hand=shand)
        return render(request,"Shop/Product.html",{'Data':data})
    else:
        return render(request,"Shop/Product.html",{'Data':data,'branddata':brand,'colordata':color,'categorydata':cat})

def delproduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return redirect("Shop:productinsertselect")

def productupdate(request,eid):
    data=tbl_product.objects.get(id=eid)
    cat = tbl_category.objects.all()
    brand = tbl_brand.objects.all()
    color = tbl_color.objects.all()
    if request.method=="POST":
        data.product_name=request.POST.get("txtname")
        data.product_details=request.POST.get("txtdetails")
        data.product_rate=request.POST.get("txtrate")
        data.product_photo=request.FILES.get("filephoto")
        sub= tbl_subcategory.objects.get(id=request.POST.get('sel_sub'))
        data.subcategory= sub
        col= tbl_color.objects.get(id=request.POST.get('sel_color'))
        data.color= col
        bran= tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        data.brand= bran
        data.save()
        return redirect("Shop:productinsertselect")
    else:
        return render(request,"Shop\Product.html",{"editdata":data,'branddata':brand,'colordata':color,'categorydata':cat})






def ajaxsubcategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcategory = tbl_subcategory.objects.filter(category=cat)
    return render(request,"Shop/AjaxSubcategory.html",{"subcategorydata":subcategory})




def addstock(request,did):
    product =  tbl_product.objects.get(id=did)
    data = tbl_stock.objects.filter(product=did)
    if request.method == "POST":
        date = request.POST.get('txtdate')
        stock_quantity = request.POST.get("txtstock")
        tbl_stock.objects.create(stock_date=date,stock_quantity=stock_quantity,product=product)

        return render(request, "Shop/AddStock.html", {'data': data})
    else:
        return render(request, "Shop/AddStock.html", {'data': data, "productdata": product})


def delstock(request,did):
    tbl_stock.objects.get(id=did).delete()
    return redirect("Shop:productInsertSelect")




def details(request,did):
    booking=tbl_productbooking.objects.get(id=did)
    data=tbl_cart.objects.filter(booking=booking)
    return render(request,"Shop\Details.html",{"Data":data,})


def vieworder(request):
    data=tbl_productbooking.objects.all()
    return render(request,"Shop\ViewOrder.html",{"Data":data,})

def updateproductbooking(request,bid):
    item = tbl_cart.objects.get(id=bid)
    if item.ship_status == 0:
        item.ship_status = 1  
    if item.ship_status == 1:
        item.ship_status = 2  
    elif item.ship_status == 2:
        item.ship_status = 3
    elif item.ship_status == 3:
        item.ship_status = 4
    elif item.ship_status == 4:
        item.ship_status = 5  
    item.save()  
    return redirect("Shop:vieworder")



def logout(request):
    if 'sid' in request.session:
        del request.session['sid']
        return redirect('guest:Login')
    else:
        return redirect('guest:Login')


def BookingReport(request):
    if request.method=="POST":
        fromdate = request.POST.get("txtfromdate")
        todate = request.POST.get("txttodate")
        data = tbl_productbooking.objects.filter(booking_date__gte=fromdate,booking_date__lte=todate)
        return render(request,"Shop/Report.html",{'data':data})
    else:
        return render(request,"Shop/Report.html")



def viewmore(request,did):
    booking=tbl_productbooking.objects.get(id=did)
    data=tbl_cart.objects.filter(booking=booking)
    return render(request,"Shop\Viewmore.html",{"Data":data,})