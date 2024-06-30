from django.db import models
from guest.models import *

# Create your models here.
class tbl_service(models.Model):
    service_name= models.CharField(max_length=50)
    service_details= models.CharField(max_length=50)
    service_rate= models.CharField(max_length=50)
    service_photo = models.FileField(upload_to='Assets/ServicePhoto/')
    center = models.ForeignKey(tbl_center, on_delete=models.CASCADE)
    servicetype = models.ForeignKey(tbl_servicetype, on_delete=models.CASCADE)
    