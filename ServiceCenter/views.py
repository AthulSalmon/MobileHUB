from django.shortcuts import render,redirect
from guest.models import *
from ServiceCenter.models import *
from administrator.models import *
from user.models import *
from django.core.mail import send_mail
# Create your views here.

def homepage(request):
    return render(request,"ServiceCenter/Homepage.html")

def my_pro(request):
    data=tbl_center.objects.get(id=request.session["cid"])
    return render(request,"ServiceCenter/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_center.objects.get(id=request.session["cid"])
    if request.method=="POST":
        prodata.center_name=request.POST.get('txtname')
        prodata.center_contact=request.POST.get('txtcon')
        prodata.center_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"ServiceCenter/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"ServiceCenter/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_center.objects.filter(id=request.session["cid"],center_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                centerdata=tbl_center.objects.get(id=request.session["cid"],center_password=request.POST.get('txtcurpass'))
                centerdata.center_password=request.POST.get('txtnewpass')
                centerdata.save()
                return render(request,"ServiceCenter/Changepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"ServiceCenter/Changepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"ServiceCenter/Changepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"ServiceCenter/Changepassword.html")






def serviceinsertselect(request):
    data=tbl_service.objects.all()
    servicetype = tbl_servicetype.objects.all()
    if request.method=="POST":
        name=request.POST.get("txtname")
        det=request.POST.get("txtdetails")
        rate=request.POST.get("txtrate")
        photo=request.FILES.get("filephoto")
        center=tbl_center.objects.get(id=request.session["cid"])
        servicetype = tbl_servicetype.objects.get(id=request.POST.get('sel_cat'))
        tbl_service.objects.create(service_name=name,service_rate=rate,service_details=det,service_photo=photo,center = center,servicetype=servicetype)
        return render(request,"ServiceCenter/Service.html",{'Data':data})
    else:
        return render(request,"ServiceCenter/Service.html",{'Data':data,'servicedata':servicetype})

def delservice(request,did):
    tbl_service.objects.get(id=did).delete()
    return redirect("ServiceCenter:serviceinsertselect")

def serviceupdate(request,eid):
    data=tbl_service.objects.get(id=eid)
    servicetype = tbl_servicetype.objects.all()
    if request.method=="POST":
        data.service_name=request.POST.get("txtname")
        data.service_details=request.POST.get("txtdetails")
        data.service_rate=request.POST.get("txtrate")
        data.service_photo=request.FILES.get("filephoto")
        ser= tbl_servicetype.objects.get(id=request.POST.get('sel_cat'))
        data.servicetype = ser
        data.save()
        return redirect("ServiceCenter:serviceinsertselect")
    else:
        return render(request,"ServiceCenter\Service.html",{"editdata":data,'servicedata':servicetype})





def vieworder(request):
    data=tbl_servicebooking.objects.filter(booking_status=0)
    return render(request,"ServiceCenter\ViewOrder.html",{"Data":data,})

def acceptbooking(request,aid):
    service=tbl_servicebooking.objects.get(id=aid) 
    service.booking_status=1
    service.save()
    user=tbl_user.objects.get(id=service.user.id)
    name=user.user_name
    email=user.user_email
    subject = 'Request Accepted'
    message = f'Dear {name}, Your Request is Accepted...\n\nThank You!!!'
    from_email = 'mobilehub9087@gmail.com' 
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect("ServiceCenter:vieworder")

def rejectedbooking(request,rid):
    service=tbl_servicebooking.objects.get(id=rid) 
    service.booking_status=2
    service.save()
    user=tbl_user.objects.get(id=service.user.id)
    name=user.user_name
    email=user.user_email
    subject = 'Request Rejected'
    message = f'Dear {name}, Your Request is Rejected...\n\nThank You!!!'
    from_email = 'mobilehub9087@gmail.com' 
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect("ServiceCenter:vieworder")

def acceptedlist(request):
    data=tbl_servicebooking.objects.filter(booking_status=1)
    return render(request,"ServiceCenter\Acceptedlist.html",{"Data":data,})

def rejectedlist(request):
    data=tbl_servicebooking.objects.filter(booking_status=2)
    return render(request,"ServiceCenter\RejectedList.html",{"Data":data,})



def logout(request):
    if 'cid' in request.session:
        del request.session['cid']
        return redirect('guest:Login')
    else:
        return redirect('guest:Login')
