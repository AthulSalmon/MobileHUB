from django.shortcuts import render,redirect
from administrator.models import *
from guest.models import *
import random
from django.core.mail import send_mail
def loadingpage(request):
    return render(request,"guest/index.html")

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        if request.POST.get('txtpwd')==request.POST.get('txtrepwd'):
            name=request.POST.get("txtname")
            email=request.POST.get("txtemail")
            place = tbl_place.objects.get(id=request.POST.get('sel_place'))
            tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_address=request.POST.get("txtadd"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
            rs=random.randint(100000,999999)
            request.session["radn"]=rs
            request.session["uemail"]=email
            request.session["uname"]=name
            subject = 'Registration Successful'
            message = f'Dear {name},\n\nOTP for login ' + str(rs) + '.\n\nThank You!!!'
            from_email = 'mobilehub9087@gmail.com' 
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("guest:Otpverify")
            # return render(request,"guest/NewUser.html",{"districtdata":district,'msg1':" Registration Successfull"})
        else:
            return render(request,"guest/NewUser.html",{"districtdata":district,'msg1':" password mismatch"})

    else:
        return render(request,"guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"guest/AjaxPlace.html",{"placedata":place})






def Login(request):
    if request.method == "POST":
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"),user_status=1).count()
        shopcount = tbl_shop.objects.filter(shop_email=request.POST.get("txt_email"),shop_password=request.POST.get("txt_password")).count()
        centercount = tbl_center.objects.filter(center_email=request.POST.get("txt_email"),center_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"),user_status=1)
            if(user.user_status==1):
                request.session["uid"] = user.id
                request.session["uname"] = user.user_name
                return redirect("user:homepage")
            elif(user.user_status==0):
                return render(request,"guest/Login.html",{"msg":"Pending"})
            else:
                return render(request,"guest/Login.html",{"msg":"Rejeted"})
        elif admincount>0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("administrator:loadinghomepage")
        elif shopcount>0:
            shop = tbl_shop.objects.get(shop_email=request.POST.get("txt_email"),shop_password=request.POST.get("txt_password"))
            if(shop.shop_status==1):
                request.session["sid"] = shop.id
                request.session["sname"] = shop.shop_name
                return redirect("Shop:homepage")
            elif(shop.shop_status==0):
                return render(request,"guest/Login.html",{"msg":"Pending"})
            else:
                return render(request,"guest/Login.html",{"msg":"Rejeted"})
        elif centercount>0:
            center = tbl_center.objects.get(center_email=request.POST.get("txt_email"),center_password=request.POST.get("txt_password"))
            if(center.center_status==1):
                request.session["cid"] = center.id
                request.session["cname"] = center.center_name
                return redirect("ServiceCenter:homepage")
            elif(shop.shop_status==0):
                return render(request,"guest/Login.html",{"msg":"Pending"})
            else:
                return render(request,"guest/Login.html",{"msg":"Rejeted"})
        return render(request,"guest/Login.html")
    else:
        return render(request,"guest/Login.html")





def ShopRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_shop.objects.create(shop_name=request.POST.get("txtname"),shop_contact=request.POST.get("txtcontact"),shop_email=request.POST.get("txtemail"),shop_address=request.POST.get("txtadd"),shop_logo=request.FILES.get("filelogo"),shop_proof=request.FILES.get("fileProof"),shop_password=request.POST.get("txtpwd"),place=place)
        return redirect("guest:ShopRegistration")
    else:
        return render(request,"guest/Shop.html",{"districtdata":district})



def ServicecenterRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_center.objects.create(center_name=request.POST.get("txtname"),center_contact=request.POST.get("txtcontact"),center_email=request.POST.get("txtemail"),center_address=request.POST.get("txtadd"),center_logo=request.FILES.get("filelogo"),center_proof=request.FILES.get("fileProof"),center_password=request.POST.get("txtpwd"),place=place)
        return redirect("guest:ServicecenterRegistration")
    else:
        return render(request,"guest/ServiceCenter.html",{"districtdata":district})



def Otpverify(request):
    
    if request.method == "POST":
        otp=request.POST.get("txtotp")
        if int(otp) == int(request.session["radn"]) :
            print("Hi")
            if request.session["uemail"] != "" and request.session["uname"] != "":
                data=tbl_user.objects.get(user_email=request.session["uemail"],user_name=request.session["uname"])
                print(data)
                data.user_status=1
                data.save()
                return redirect("guest:Login")
            else:
                return render(request,"Guest/OTPVerification.html",{'msg':"Error!!!!!"})
        else:
            return render(request,"Guest/OTPVerification.html",{'msg':"Invalid OTP!!"})
    else:
        return render(request,"Guest/OTPVerification.html")

