from django.shortcuts import render,redirect
from administrator.models import *
from guest.models import *
from user.models import *
from datetime import date
# Create your views here.




def loadinghomepage(request):
    return render(request,"administrator/Homepage.html")



def Districtinsertselect(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("txtdistrict")
        tbl_district.objects.create(district_name=district)
        return render(request,"administrator/District.html",{'Data':disdata})
    else:
        return render(request,"administrator/District.html",{'Data':disdata})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("administrator:Districtinsertselect")

def districtupdate(request,eid):
    data=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        data.district_name=request.POST.get("txtdistrict")
        data.save()
        return redirect("administrator:Districtinsertselect")
    else:
        return render(request,"administrator\District.html",{"editdata":data})







def Categoryinsertselect(request):
    catdata=tbl_category.objects.all()
    if request.method=="POST":
        cat=request.POST.get("txtcategory")
        tbl_category.objects.create(category_name=cat)
        return render(request,"administrator/Category.html",{'Data':catdata})
    else:
        return render(request,"administrator/Category.html",{'Data':catdata})
def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("administrator:Categoryinsertselect")

def categoryupdate(request,eid):
    data=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        data.category_name=request.POST.get("txtcategory")
        data.save()
        return redirect("administrator:Categoryinsertselect")
    else:
        return render(request,"administrator\Category.html",{"editdata":data})









def Placeinsertselect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtplace')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"administrator/Place.html",{'data':data})
    else:
        return render(request,"administrator/Place.html",{'data':data,"districtdata":district})
def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("administrator:Placeinsertselect")
def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtplace")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("administrator:Placeinsertselect")
    else:
        return render(request,"administrator\Place.html",{"editdata":editdata,"districtdata":district})






def admininsertselect(request):
    admindata=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get("txtname")
        email=request.POST.get("txtemail")
        phn=request.POST.get("txtphn")
        pass1=request.POST.get("txtpass")
        pass2=request.POST.get("txtcpass")
        if pass1==pass2:
            tbl_admin.objects.create(admin_name=name,admin_email=email,admin_phoneno=phn,admin_password=pass1)
            return render(request,"administrator/admin.html",{'Data':admindata})
        else:
            print("Password miss")
            return render(request,"administrator/admin.html",{'Data':admindata})
    else:
        return render(request,"administrator/admin.html",{'Data':admindata})







def Departmentinsertselect(request):
    disdata=tbl_department.objects.all()
    if request.method=="POST":
        dept=request.POST.get("txtdept")
        tbl_department.objects.create(dept_name=dept)
        return render(request,"administrator/Department.html",{'Data':disdata})
    else:
        return render(request,"administrator/Department.html",{'Data':disdata})
def delDepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect("administrator:Departmentinsertselect")

def departmentupdate(request,eid):
    data=tbl_department.objects.get(id=eid)
    if request.method=="POST":
        data.dept_name=request.POST.get("txtdept")
        data.save()
        return redirect("administrator:Departmentinsertselect")
    else:
        return render(request,"administrator\Department.html",{"editdata":data})    








def Designationinsertselect(request):
    disdata=tbl_designation.objects.all()
    if request.method=="POST":
        Designation=request.POST.get("txtdesignation")
        tbl_designation.objects.create(designation_name=Designation)
        return render(request,"administrator/Designation.html",{'Data':disdata})
    else:
        return render(request,"administrator/Designation.html",{'Data':disdata})
def delDesignation(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect("administrator:Designationinsertselect")

def designationupdate(request,eid):
    data=tbl_designation.objects.get(id=eid)
    if request.method=="POST":
        data.designation_name=request.POST.get("txtdesignation")
        data.save()
        return redirect("administrator:Designationinsertselect")
    else:
        return render(request,"administrator\Designation.html",{"editdata":data})         










def Subjectinsertselect(request):
    disdata=tbl_subject.objects.all()
    if request.method=="POST":
        subject=request.POST.get("txtsub")
        tbl_subject.objects.create(sub_name=subject)
        return render(request,"administrator/Subject.html",{'Data':disdata})
    else:
        return render(request,"administrator/Subject.html",{'Data':disdata})


def delSubject(request,did):
    tbl_subject.objects.get(id=did).delete()
    return redirect("administrator:Subjectinsertselect")

def subjectupdate(request,eid):
    data=tbl_subject.objects.get(id=eid)
    if request.method=="POST":
        data.sub_name=request.POST.get("txtsub")
        data.save()
        return redirect("administrator:Subjectinsertselect")
    else:
        return render(request,"administrator\Subject.html",{"editdata":data})   










def Semesterinsertselect(request):
    disdata=tbl_semester.objects.all()
    if request.method=="POST":
        sem=request.POST.get("txtsem")
        tbl_semester.objects.create(sem_name=sem)
        return render(request,"administrator/Semester.html",{'Data':disdata})
    else:
        return render(request,"administrator/Semester.html",{'Data':disdata})
def delSemester(request,did):
    tbl_semester.objects.get(id=did).delete()
    return redirect("administrator:Semesterinsertselect")

def semesterupdate(request,eid):
    data=tbl_semester.objects.get(id=eid)
    if request.method=="POST":
        data.sem_name=request.POST.get("txtsem")
        data.save()
        return redirect("administrator:Semesterinsertselect")
    else:
        return render(request,"administrator\Semester.html",{"editdata":data})                     






def Employeeinsertselect(request):
    department = tbl_department.objects.all()
    designation = tbl_designation.objects.all()
    data=tbl_employee.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get("txtemail")
        phn=request.POST.get("txtphn")
        designation = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        dept = tbl_department.objects.get(id=request.POST.get('sel_dept'))
        sal=request.POST.get("txtsalary")
        tbl_employee.objects.create(emp_name=name,emp_contact=phn,emp_email=email,designation=designation,department=dept,emp_salary=sal)
        return render(request,"administrator/Employee.html",{'data':data})
    else:
        return render(request,"administrator/Employee.html",{'data':data,"deptdata":department,"designationdata":designation})
def delemployee(request,did):
    tbl_employee.objects.get(id=did).delete()
    return redirect("administrator:Employeeinsertselect")
def employeeupdate(request,eid):
    designation = tbl_designation.objects.all()
    department = tbl_department.objects.all()
    editdata=tbl_employee.objects.get(id=eid)
    if request.method=="POST":
        editdata.emp_name=request.POST.get("txtname")
        editdata.emp_contact=request.POST.get("txtphn")
        editdata.emp_email=request.POST.get("txtemail")
        editdata.emp_salary=request.POST.get("txtsalary")
        dept = tbl_department.objects.get(id=request.POST.get('sel_dept'))
        desi = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        editdata.department = dept
        editdata.designation = desi
        editdata.save()
        return redirect("administrator:Employeeinsertselect")
    else:
        return render(request,"administrator\Employee.html",{"editdata":editdata,"designationdata":designation,"deptdata":department})








def Courseinsertselect(request):
    department = tbl_department.objects.all()
    data=tbl_course.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtcourse')
        duration=request.POST.get("txtdur")
        sem=request.POST.get("txtsem")
        dept = tbl_department.objects.get(id=request.POST.get('sel_dept'))
        tbl_course.objects.create(c_name=name,c_sem=sem,c_duration=duration,department=dept)
        return render(request,"administrator/Course.html",{'data':data})
    else:
        return render(request,"administrator/Course.html",{'data':data,"deptdata":department})
def delcourse(request,did):
    tbl_course.objects.get(id=did).delete()
    return redirect("administrator:Courseinsertselect")
def courseupdate(request,eid):
    department = tbl_department.objects.all()
    editdata=tbl_course.objects.get(id=eid)
    if request.method=="POST":
        editdata.c_name=request.POST.get("txtcourse")
        editdata.c_duration=request.POST.get("txtdur")
        editdata.c_sem=request.POST.get("txtsem")
        dept = tbl_department.objects.get(id=request.POST.get('sel_dept'))
        editdata.department = dept
        editdata.save()
        return redirect("administrator:Courseinsertselect")
    else:
        return render(request,"administrator\Course.html",{"editdata":editdata,"deptdata":department})






def Syllabusinsertselect(request):
    course = tbl_course.objects.all()
    subject = tbl_subject.objects.all()
    semester = tbl_semester.objects.all()
    data=tbl_syllabus.objects.all()
    if request.method=="POST":
        subject = tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        course = tbl_course.objects.get(id=request.POST.get('sel_course'))
        sem = tbl_semester.objects.get(id=request.POST.get('sel_sem'))
        tbl_syllabus.objects.create(subject=subject,course=course,semester=sem)
        return render(request,"administrator/Syllabus.html",{'data':data})
    else:
        return render(request,"administrator/Syllabus.html",{'data':data,"coursedata":course,"semdata":semester,"subjectdata":subject})
def delsyllabus(request,did):
    tbl_syllabus.objects.get(id=did).delete()
    return redirect("administrator:Syllabusinsertselect")
def syllabusupdate(request,eid):
    course = tbl_course.objects.all()
    subject = tbl_subject.objects.all()
    semester = tbl_semester.objects.all()
    editdata=tbl_syllabus.objects.get(id=eid)
    if request.method=="POST":
        sub = tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        coue = tbl_course.objects.get(id=request.POST.get('sel_course'))
        sem = tbl_semester.objects.get(id=request.POST.get('sel_sem'))
        editdata.subject = sub
        editdata.course = coue
        editdata.semester = sem
        editdata.save()
        return redirect("administrator:Syllabusinsertselect")
    else:
        return render(request,"administrator\Syllabus.html",{"editdata":editdata,"coursedata":course,"semdata":semester,"subjectdata":subject})



def User(request):
    data=tbl_user.objects.filter(user_status=0)
    return render(request,"administrator\Viewuser.html",{"data":data,})

def acceptuser(request,aid):
    user=tbl_user.objects.get(id=aid) 
    user.user_status=1
    user.save()
    return redirect("administrator:loadinghomepage")

def rejecteduser(request,rid):
    user=tbl_user.objects.get(id=rid) 
    user.user_status=2
    user.save()
    return redirect("administrator:loadinghomepage")

def acceptuserlist(request):
    data=tbl_user.objects.filter(user_status=1)
    return render(request,"administrator\Accepteduser.html",{"data":data,})

def rejecteduserlist(request):
    data=tbl_user.objects.filter(user_status=2)
    return render(request,"administrator\Rejecteduser.html",{"data":data,})






def Shop(request):
    data=tbl_shop.objects.filter(shop_status=0)
    return render(request,"administrator\Viewshop.html",{"data":data,})

def acceptshop(request,aid):
    shop=tbl_shop.objects.get(id=aid) 
    shop.shop_status=1
    shop.save()
    return redirect("administrator:loadinghomepage")

def rejectedshop(request,rid):
    shop=tbl_shop.objects.get(id=rid) 
    shop.shop_status=2
    shop.save()
    return redirect("administrator:loadinghomepage")

def acceptshoplist(request):
    data=tbl_shop.objects.filter(shop_status=1)
    return render(request,"administrator\Acceptedshop.html",{"data":data,})

def rejectedshoplist(request):
    data=tbl_shop.objects.filter(shop_status=2)
    return render(request,"administrator\Rejectedshop.html",{"data":data,})







def Subcategoryinsertselect(request):
    category = tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcatName=request.POST.get('txtsub')
        cat = tbl_category.objects.get(id=request.POST.get('sel_cat'))
        tbl_subcategory.objects.create(subcat_name=subcatName,category=cat)
        return render(request,"administrator/Subcategory.html",{'data':data})
    else:
        return render(request,"administrator/Subcategory.html",{'data':data,"catdata":category})
def delsubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("administrator:Subcategoryinsertselect")
def subcategoryupdate(request,eid):
    category = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.subcat_name=request.POST.get("txtsub")
        cat = tbl_category.objects.get(id=request.POST.get('sel_cat'))
        editdata.category = cat
        editdata.save()
        return redirect("administrator:Subcategoryinsertselect")
    else:
        return render(request,"administrator\Subcategory.html",{"editdata":editdata,"catdata":category})






def ComplaintListNew(request):

    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)

    freedata=tbl_freelancer.objects.all()
    freeComplaint=tbl_complaint.objects.filter(complaint_status=0,freelancer__in=freedata)

    instdata=tbl_institute.objects.all()
    instComplaint=tbl_complaint.objects.filter(complaint_status=0,inst__in=instdata)

    return render(request,"administrator/ComplaintListNew.html",{'userComplaint':userComplaint,'freeComplaint':freeComplaint,'instComplaint':instComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("administrator:loadinghomepage")
    else:
        return render(request,"administrator/ComplaintListReply.html",{'complaint':complaint})

    



#Complaint
def complaintSelect(request):
    userdata=tbl_user.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"administrator/Newcomplaint.html",{'data':data})
    

def complaintreplayInsert(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("administrator:complaintSelect")
    else:
        return render(request,"administrator/Complaintreplay.html",{'complaint':complaint})

def complaintsolvedSelect(request):
    userdata=tbl_user.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"administrator/Solvedcomplaint.html",{'data':data})








def servicetypeinsertselect(request):
    data=tbl_servicetype.objects.all()
    if request.method=="POST":
        servicetype=request.POST.get("txtservice")
        tbl_servicetype.objects.create(stype_name=servicetype)
        return render(request,"administrator/ServiceType.html",{'Data':data})
    else:
        return render(request,"administrator/ServiceType.html",{'Data':data})

def delservicetype(request,did):
    tbl_servicetype.objects.get(id=did).delete()
    return redirect("administrator:servicetypeinsertselect")

def servicetypeupdate(request,eid):
    data=tbl_servicetype.objects.get(id=eid)
    if request.method=="POST":
        data.stype_name=request.POST.get("txtservice")
        data.save()
        return redirect("administrator:servicetypeinsertselect")
    else:
        return render(request,"administrator\ServiceType.html",{"editdata":data})



#ROM

def rominsertselect(request):
    data=tbl_rom.objects.all()
    if request.method=="POST":
        rom=request.POST.get("txtrom")
        tbl_rom.objects.create(rom_name=rom)
        return render(request,"administrator/ROM.html",{'Data':data})
    else:
        return render(request,"administrator/ROM.html",{'Data':data})

def delrom(request,did):
    tbl_rom.objects.get(id=did).delete()
    return redirect("administrator:rominsertselect")

def romupdate(request,eid):
    data=tbl_rom.objects.get(id=eid)
    if request.method=="POST":
        data.rom_name=request.POST.get("txtrom")
        data.save()
        return redirect("administrator:rominsertselect")
    else:
        return render(request,"administrator\ROM.html",{"editdata":data})




def raminsertselect(request):
    data=tbl_ram.objects.all()
    if request.method=="POST":
        ram=request.POST.get("txtram")
        tbl_ram.objects.create(ram_name=ram)
        return render(request,"administrator/Ram.html",{'Data':data})
    else:
        return render(request,"administrator/Ram.html",{'Data':data})

def delram(request,did):
    tbl_ram.objects.get(id=did).delete()
    return redirect("administrator:raminsertselect")

def ramupdate(request,eid):
    data=tbl_ram.objects.get(id=eid)
    if request.method=="POST":
        data.ram_name=request.POST.get("txtram")
        data.save()
        return redirect("administrator:raminsertselect")
    else:
        return render(request,"administrator\Ram.html",{"editdata":data})





def colorinsertselect(request):
    data=tbl_color.objects.all()
    if request.method=="POST":
        color=request.POST.get("txtcolor")
        tbl_color.objects.create(color_name=color)
        return render(request,"administrator/Color.html",{'Data':data})
    else:
        return render(request,"administrator/Color.html",{'Data':data})

def delcolor(request,did):
    tbl_color.objects.get(id=did).delete()
    return redirect("administrator:colorinsertselect")

def colorupdate(request,eid):
    data=tbl_color.objects.get(id=eid)
    if request.method=="POST":
        data.color_name=request.POST.get("txtcolor")
        data.save()
        return redirect("administrator:colorinsertselect")
    else:
        return render(request,"administrator\Color.html",{"editdata":data})





def brandinsertselect(request):
    data=tbl_brand.objects.all()
    if request.method=="POST":
        brand=request.POST.get("txtbrand")
        tbl_brand.objects.create(brand_name=brand)
        return render(request,"administrator/Brand.html",{'Data':data})
    else:
        return render(request,"administrator/Brand.html",{'Data':data})

def delbrand(request,did):
    tbl_brand.objects.get(id=did).delete()
    return redirect("administrator:brandinsertselect")

def brandupdate(request,eid):
    data=tbl_brand.objects.get(id=eid)
    if request.method=="POST":
        data.brand_name=request.POST.get("txtbrand")
        data.save()
        return redirect("administrator:brandinsertselect")
    else:
        return render(request,"administrator\Brand.html",{"editdata":data})











def Center(request):
    data=tbl_center.objects.filter(center_status=0)
    return render(request,"administrator\Viewcenter.html",{"data":data,})

def acceptcenter(request,aid):
    center=tbl_center.objects.get(id=aid) 
    center.center_status=1
    center.save()
    return redirect("administrator:loadinghomepage")

def rejectedcenter(request,rid):
    center=tbl_center.objects.get(id=rid) 
    center.center_status=2
    center.save()
    return redirect("administrator:loadinghomepage")

def acceptcenterlist(request):
    data=tbl_center.objects.filter(center_status=1)
    return render(request,"administrator\Acceptedcenter.html",{"data":data,})

def rejectedcenterlist(request):
    data=tbl_center.objects.filter(center_status=2)
    return render(request,"administrator\Rejectedcenter.html",{"data":data,})


def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('guest:Login')
    else:
        return redirect('guest:Login')
def logout(request):
    if 'aid' in request.session:
        del request.session['aid']
        return redirect('guest:Login')
    else:
        return redirect('guest:Login')
