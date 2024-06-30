from django.db import models


class tbl_district(models.Model):
    district_name = models.CharField(max_length=50)


class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_phoneno=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)


class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    subcat_name=models.CharField(max_length=50)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)


class tbl_department(models.Model):
    dept_name= models.CharField(max_length=50)



class tbl_designation(models.Model):
    designation_name= models.CharField(max_length=50)


class tbl_subject(models.Model):
    sub_name= models.CharField(max_length=50)


class tbl_semester(models.Model):
    sem_name= models.CharField(max_length=50)





class tbl_employee(models.Model):
    emp_name= models.CharField(max_length=50)
    emp_contact= models.CharField(max_length=50)
    emp_email= models.CharField(max_length=50)
    designation = models.ForeignKey(tbl_designation, on_delete=models.CASCADE)
    department = models.ForeignKey(tbl_department, on_delete=models.CASCADE)
    emp_salary= models.CharField(max_length=50)



class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)







class tbl_course(models.Model):
    c_name= models.CharField(max_length=50)
    c_duration= models.CharField(max_length=50)
    c_sem= models.CharField(max_length=50)
    department = models.ForeignKey(tbl_department, on_delete=models.CASCADE)


class tbl_syllabus(models.Model):
    course = models.ForeignKey(tbl_course, on_delete=models.CASCADE)
    subject = models.ForeignKey(tbl_subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(tbl_semester, on_delete=models.CASCADE)
   
    









    


class tbl_servicetype(models.Model):
    stype_name=models.CharField(max_length=50)




class tbl_ram(models.Model):
    ram_name=models.CharField(max_length=50)




class tbl_rom(models.Model):
    rom_name=models.CharField(max_length=50)


class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)


class tbl_color(models.Model):
    color_name=models.CharField(max_length=50)
