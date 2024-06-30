from django.db import models
from administrator.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_address=models.CharField(max_length=500)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")




class tbl_shop(models.Model):
    shop_name=models.CharField(max_length=50)
    shop_address=models.CharField(max_length=500)
    shop_contact=models.CharField(max_length=50)
    shop_email=models.CharField(max_length=50)
    shop_password=models.CharField(max_length=50)
    shop_logo = models.FileField(upload_to='Assets/ShopLogo/')
    shop_proof = models.FileField(upload_to='Assets/Shopproof/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    shop_status = models.IntegerField(default="0")






class tbl_center(models.Model):
    center_name=models.CharField(max_length=50)
    center_address=models.CharField(max_length=500)
    center_contact=models.CharField(max_length=50)
    center_email=models.CharField(max_length=50)
    center_password=models.CharField(max_length=50)
    center_logo = models.FileField(upload_to='Assets/CenterLogo/')
    center_proof = models.FileField(upload_to='Assets/Centerproof/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    center_status = models.IntegerField(default="0")
    