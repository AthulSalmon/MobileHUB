from django.db import models
from guest.models import *
from administrator.models import *


class tbl_product(models.Model):
    product_name= models.CharField(max_length=50)
    product_details= models.CharField(max_length=500)
    product_rate= models.CharField(max_length=50)
    product_photo = models.FileField(upload_to='Assets/ProductPhoto/')
    shop= models.ForeignKey(tbl_shop, on_delete=models.CASCADE)
    brand= models.ForeignKey(tbl_brand, on_delete=models.CASCADE)
    subcategory= models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
    color= models.ForeignKey(tbl_color, on_delete=models.CASCADE)
    second_hand=models.CharField(max_length=100,null=True)
  
    

class tbl_stock(models.Model):
    stock_quantity=models.IntegerField()
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    stock_date=models.DateField(null=True)
