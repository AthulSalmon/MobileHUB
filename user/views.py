from django.shortcuts import render,redirect
from administrator.models import *
from guest.models import *
from user.models import *
from ServiceCenter.models import *
from Shop.models import *
from datetime import date
from django.db.models import Sum
from django.http import JsonResponse
import random
from datetime import datetime


def homepage(request):
    return render(request,"user/Homepage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"user/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"user/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"user/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"user/Changepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"user/Changepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"user/Changepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"user/Changepassword.html")



def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    user=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('textcomp')
        tbl_complaint.objects.create(complaint_title=title,complaint_detail=details,user=user)
        return redirect("user:POSTComplaint")
    else:
        return render(request,"user/Complaint.html",{"data":data})

def complaintDelete(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("user:POSTComplaint")








# def productbooking(request):
#     data=tbl_product.objects.all()
#     for product in data:
#         total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_quantity'))['total']
#         total_cart = tbl_cart.objects.filter(product=product.id).aggregate(total=Sum('cart_qty'))['total']
#         print(total_stock,"stock")
#         print(total_cart,"cart")
#         if total_stock is None:
#             total_stock = 0
#         if total_cart is None:
#             total_cart = 0
#         if isinstance(total_stock, int):
#             total_stock = total_stock
#         else:
#             total_stock = 0     
#             if isinstance(total_cart, int):
#                 total_cart = total_cart
#             else:
#                 total_cart = 0
#         total=  total_stock-total_cart
#         product.total_stock = total
#     return render(request, "user\Booking.html", {"Data": data, "total_stock": total_stock})


def productbooking(request):
    ar=[1,2,3,4,5]
    data = tbl_product.objects.filter(second_hand="No")
    avg_list = []  

    reviewcount = 0
    for product in data:
        total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_cart.objects.filter(product=product.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        total = total_stock - total_cart
        product.total = total
    for c in data:
        reviewcount = tbl_review.objects.filter(product=c.id).count()
        # print(reviewcount)
        res = 0
        avg = 0
        review = tbl_review.objects.filter(product=c.id)
        for rev in review:
            res = res + rev.user_rating
            # print(res)
            avg = res//reviewcount
            # print(avg)
        avg_list.append(avg)
    print(avg_list)
    cdata = zip(data,avg_list)
    return render(request, "user/Booking.html", {"Data": cdata,"avg": avg_list,"ar":ar})


def productsearch(request):
    data= tbl_product.objects.filter(product_name__istartswith=request.GET.get('word'))
    return render(request,"user/AjaxSearchProduct.html",{"data":data})



def viewmore(request, vid):
    data = tbl_product.objects.filter(id=vid)
    return render(request,"user/ViewMore.html",{'data': data})




def productbook(request,did):
    product=tbl_product.objects.get(id=did)
    user=tbl_user.objects.get(id=request.session["uid"])
    count = tbl_productbooking.objects.filter(user=user,booking_status=0).count()
    if count > 0:
        bcount=tbl_productbooking.objects.get(user=user,booking_status=0)
        icount=tbl_cart.objects.filter(product=product,booking=bcount).count()
        if icount > 0:
           return render(request,"user/Booking.html",{'msg':"Already Added"}) 
        else:
            tbl_cart.objects.create(booking=bcount,product=product,cart_qty=1)
            return render(request,"user/Booking.html",{'msg':"Added to Cart"})
    else:
        tbl_productbooking.objects.create(user=user)
        count = tbl_productbooking.objects.filter(user=user,booking_status=0).count()
        if count > 0:
            bcount=tbl_productbooking.objects.get(user=user,booking_status=0)
            icount=tbl_cart.objects.filter(product=product,booking=bcount).count()
            if icount > 0:
                return render(request,"user/Booking.html",{'msg':"Already Added"}) 
            else:
                tbl_cart.objects.create(booking=bcount,product=product,cart_qty=1)
                return render(request,"user/Booking.html",{'msg':"Added to Cart"})


def payment(request):
    if request.method=="POST":
        bookingdata=tbl_productbooking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_status=2
        bookingdata.save()
        id=bookingdata.id
        return redirect("user:Billing",did=id)
    else: 
        return render(request,"user/Payment.html")


def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_productbooking.objects.get(id=request.session["bookingid"])
        cart=tbl_cart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status=1
            i.save()
        bookingdata.price=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("user:payment")
    else:
        customerdata=tbl_user.objects.get(id=request.session["uid"])
        bcount=tbl_productbooking.objects.filter(user=customerdata,booking_status=0).count()
        if bcount>0:
            book=tbl_productbooking.objects.get(user=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_productbooking.objects.get(id=bid)
            cartdata=tbl_cart.objects.filter(booking=bkid)
            data=[]
            for product in cartdata:
                total_stock = tbl_stock.objects.filter(product=product.product_id).aggregate(total=Sum('stock_quantity'))['total']
                total_cart = tbl_cart.objects.filter(product=product.product_id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                if isinstance(total_stock, int):
                    total_stock = total_stock
                else:
                    total_stock = 0
                    
                if isinstance(total_cart, int):
                    total_cart = total_cart
                else:
                    total_cart = 0
                total=  total_stock-total_cart
                print (total)
                print("stock",total_stock)
                print("cart",total_cart)
                product.stock = total
                pro_data={
                    'id':product.id,
                    'cartproduct': product,
                    'stock':total,
                }
                data.append(pro_data)
            
            return render(request,"user/MyCart.html",{'data':data})
        else:
            return render(request,"user/MyCart.html")
    
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("user:mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("user:mycart")


# def details(request,did):
#     booking=tbl_productbooking.objects.get(id=did)
#     data=tbl_cart.objects.filter(booking=booking)
#     return render(request,"user\Details.html",{"Data":data,})


def myorder(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    data1 = tbl_productbooking.objects.filter(user=user,booking_status=2)
    data = tbl_cart.objects.filter(booking__in=data1)
    return render(request, "user\Myorder.html", {"Data": data})





def cancel(request,cid):
    data=tbl_cart.objects.get(id=cid) 
    data.cart_status=2
    data.save()
    return redirect("user:myorder")

def rating(request,cid):
    
        parray=[1,2,3,4,5]
        cid=cid
        cdata=tbl_product.objects.get(id=cid)
        wdata=tbl_user.objects.get(id=request.session["uid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(product=cdata).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(product=cdata).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"user/Review.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"user/Review.html",{'cid':cid})
    

def ajaxrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    product=request.GET.get('workid')
    cdata=tbl_product.objects.get(id=product)
    cust=tbl_user.objects.get(id=request.session["uid"])
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,product=cdata,user=cust)
    stardata=tbl_review.objects.filter(product=product).order_by('-review_datetime')
    return render(request,"user/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    pro_id = request.GET.get("pdt")
    cdata = tbl_product.objects.get(id=pro_id)
    rate = tbl_review.objects.filter(product=cdata)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)





def servicebooking(request):
    data=tbl_service.objects.all()
    ar=[1,2,3,4,5]
    avg_list = []  

    reviewcount = 0
    servicedata=tbl_servicetype.objects.all()
    for c in data:
        reviewcount = tbl_review.objects.filter(service=c.id).count()
        # print(reviewcount)
        res = 0
        avg = 0
        review = tbl_review.objects.filter(service=c.id)
        for rev in review:
            res = res + rev.user_rating
            # print(res)
            avg = res//reviewcount
            # print(avg)
        avg_list.append(avg)
    print(avg_list)
    cdata = zip(data,avg_list)
    return render(request,"user\BookService.html",{"data":cdata,"servicedata":servicedata,"avg": avg_list,"ar":ar})

def search(request):
    servicedata= tbl_servicetype.objects.get(id=request.GET.get("did"))
    data= tbl_service.objects.filter(servicetype=servicedata)
    return render(request,"user/AjaxServiceSearch.html",{"data":data})


def servicerating(request,cid):
    
        parray=[1,2,3,4,5]
        cid=cid
        cdata=tbl_service.objects.get(id=cid)
        wdata=tbl_user.objects.get(id=request.session["uid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(service=cdata).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(service=cdata).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"user/ServiceReview.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"user/ServiceReview.html",{'cid':cid})
    

def ajaxservicerating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    service=request.GET.get('workid')
    cdata=tbl_service.objects.get(id=service)
    cust=tbl_user.objects.get(id=request.session["uid"])
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,service=cdata,user=cust)
    stardata=tbl_review.objects.filter(service=service).order_by('-review_datetime')
    return render(request,"user/AjaxServiceRating.html",{'data':stardata,'ar':parray})

def starservicerating(request):
    r_len = 0
    five = four = three = two = one = 0
    pro_id = request.GET.get("pdt")
    cdata = tbl_service.objects.get(id=pro_id)
    rate = tbl_review.objects.filter(service=cdata)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)

def appointment(request,aid):
    service=tbl_service.objects.get(id=aid)
    if request.method == "POST":
        complaint_detail=request.POST.get('txtcom')
        user_number=request.POST.get('txtnum')
        pickup=request.POST.get('pickup')
        fordate = request.POST.get('txtdate')
        fortime = request.POST.get('txttime')
        details = request.POST.get('txtdetail')
        user = tbl_user.objects.get(id=request.session["uid"])

        tbl_servicebooking.objects.create(
            booking_fordate=fordate,
            booking_fortime=fortime,
            service=service,
            user=user,
            booking_detail=details,
            user_number=user_number,
            complaint_detail=complaint_detail,
            pickup=pickup
            

        )

        return redirect("user:servicebooking")
    else:
        return render(request, "user/Appointment.html")



def mybooking(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_servicebooking.objects.filter(user=user)
    return render(request,"user\Mybooking.html",{"Data":data})


def Billing(request,did):
    billno = random.randint(10000, 99999)
    today = datetime.now().strftime("%d-%m-%Y")
    cust = tbl_user.objects.get(id=request.session["uid"])
    
    latest_booking = tbl_productbooking.objects.get(user=cust, booking_status=2,id=did)
    
    data = tbl_cart.objects.filter(booking=latest_booking)
    total=latest_booking.price
    return render(request,"User/Bill.html",{'billno':billno,'today':today,'userdata':cust,'data':data,'total':total})

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('guest:Login')
    else:
        return redirect('guest:Login')



def viewproduct(request):
    ar=[1,2,3,4,5]
    data = tbl_product.objects.filter(second_hand="Yes")
    avg_list = []  

    reviewcount = 0
    for product in data:
        total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_cart.objects.filter(product=product.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        total = total_stock - total_cart
        product.total = total
    for c in data:
        reviewcount = tbl_review.objects.filter(product=c.id).count()
        # print(reviewcount)
        res = 0
        avg = 0
        review = tbl_review.objects.filter(product=c.id)
        for rev in review:
            res = res + rev.user_rating
            # print(res)
            avg = res//reviewcount
            # print(avg)
        avg_list.append(avg)
    print(avg_list)
    cdata = zip(data,avg_list)
    return render(request, "user/Viewproduct.html", {"Data": cdata,"avg": avg_list,"ar":ar})

