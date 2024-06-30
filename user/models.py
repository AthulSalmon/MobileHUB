from django.db import models
from guest.models import *
from Shop.models import *
from ServiceCenter.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_detail=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50)
    complaint_replydate=models.DateField(null=True)
    complaint_status=models.IntegerField(default="0")



class tbl_servicebooking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_detail=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    service = models.ForeignKey(tbl_service, on_delete=models.CASCADE)
    booking_status=models.IntegerField(default="0")
    booking_fortime=models.CharField(max_length=50)
    booking_fordate=models.DateField(null=True)
    complaint_detail=models.CharField(max_length=50)
    pickup=models.CharField(max_length=10)
    user_number=models.CharField(max_length=50)


class tbl_productbooking(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    booking_status = models.IntegerField(default="0")
    price = models.CharField(default="0",max_length=40)



class tbl_cart(models.Model):
    booking = models.ForeignKey(tbl_productbooking, on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    cart_qty= models.CharField(max_length=500)
    cart_status=models.IntegerField(default="0")
    ship_status=models.IntegerField(default="0")


class tbl_review(models.Model):
    user_rating=models.IntegerField(max_length=20)
    user_review=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    review_datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    product= models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)
    service= models.ForeignKey(tbl_service,on_delete=models.CASCADE,null=True)

    