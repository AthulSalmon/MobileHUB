from django.urls import path,include
from administrator import views

app_name="administrator"


urlpatterns = [



    path('Homepage/',views.loadinghomepage,name='loadinghomepage'),


    path('Districtinsertselect/',views.Districtinsertselect,name="Districtinsertselect"),
    path('delDistrict/<int:did>',views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),


    path('Categoryinsertselect/',views.Categoryinsertselect,name="Categoryinsertselect"),
    path('delcategory/<int:did>',views.delcategory,name="delcategory"),
    path('categoryupdate/<int:eid>',views.categoryupdate,name="categoryupdate"),




    path('Placeinsertselect/',views.Placeinsertselect,name="Placeinsertselect"),
    path('delplace/<int:did>',views.delplace,name="delplace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),



    path('admininsertselect/',views.admininsertselect,name="admininsertselect"),




    path('Departmentinsertselect/',views.Departmentinsertselect,name="Departmentinsertselect"),
    path('delDepartment/<int:did>',views.delDepartment,name="delDepartment"),
    path('departmentupdate/<int:eid>',views.departmentupdate,name="departmentupdate"),


    path('Designationinsertselect/',views.Designationinsertselect,name="Designationinsertselect"),
    path('delDesignation/<int:did>',views.delDesignation,name="delDesignation"),
    path('designationupdate/<int:eid>',views.designationupdate,name="designationupdate"),





    path('Subjectinsertselect/',views.Subjectinsertselect,name="Subjectinsertselect"),
    path('delSubject/<int:did>',views.delSubject,name="delSubject"),
    path('subjectupdate/<int:eid>',views.subjectupdate,name="subjectupdate"),



    path('Semesterinsertselect/',views.Semesterinsertselect,name="Semesterinsertselect"),
    path('delSemester/<int:did>',views.delSemester,name="delSemester"),
    path('semesterupdate/<int:eid>',views.semesterupdate,name="semesterupdate"),




    path('Employeeinsertselect/',views.Employeeinsertselect,name="Employeeinsertselect"),
    path('delemployee/<int:did>',views.delemployee,name="delemployee"),
    path('employeeupdate/<int:eid>',views.employeeupdate,name="employeeupdate"),




    path('Courseinsertselect/',views.Courseinsertselect,name="Courseinsertselect"),
    path('delcourse/<int:did>',views.delcourse,name="delcourse"),
    path('courseupdate/<int:eid>',views.courseupdate,name="courseupdate"),



    path('Syllabusinsertselect/',views.Syllabusinsertselect,name="Syllabusinsertselect"),
    path('delsyllabus/<int:did>',views.delsyllabus,name="delsyllabus"),
    path('syllabusupdate/<int:eid>',views.syllabusupdate,name="syllabusupdate"),




    path('Viewuser/',views.User,name='User'),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejecteduser/<int:rid>',views.rejecteduser,name="rejecteduser"),
    path('acceptuserlist/',views.acceptuserlist,name='acceptuserlist'),
    path('rejecteduserlist/',views.rejecteduserlist,name='rejecteduserlist'),
   
   
   
   
   
    
    
    path('Subcategoryinsertselect/',views.Subcategoryinsertselect,name="Subcategoryinsertselect"),
    path('delsubcategory/<int:did>',views.delsubcategory,name="delsubcategory"),
    path('subcategoryupdate/<int:eid>',views.subcategoryupdate,name="subcategoryupdate"),



    #Complaint
    path('ComplaintView/',views.complaintSelect,name="complaintSelect"),
    path('ComplaintReply/<int:cid>',views.complaintreplayInsert,name="complaintreplayInsert"),
    path('ComplaintSolvedView/',views.complaintsolvedSelect,name="complaintsolvedSelect"),



    #Service Type
    path('servicetypeinsertselect/',views.servicetypeinsertselect,name="servicetypeinsertselect"),
    path('delservicetype/<int:did>',views.delservicetype,name="delservicetype"),
    path('servicetypeupdate/<int:eid>',views.servicetypeupdate,name="servicetypeupdate"),



    #RAM
    path('raminsertselect/',views.raminsertselect,name="raminsertselect"),
    path('delram/<int:did>',views.delram,name="delram"),
    path('ramupdate/<int:eid>',views.ramupdate,name="ramupdate"),


    #ROM
    path('rominsertselect/',views.rominsertselect,name="rominsertselect"),
    path('delrom/<int:did>',views.delrom,name="delrom"),
    path('romupdate/<int:eid>',views.romupdate,name="romupdate"),



    #Brand
    path('brandinsertselect/',views.brandinsertselect,name="brandinsertselect"),
    path('delbrand/<int:did>',views.delbrand,name="delbrand"),
    path('brandupdate/<int:eid>',views.brandupdate,name="brandupdate"),


    #color
    path('colorinsertselect/',views.colorinsertselect,name="colorinsertselect"),
    path('delcolor/<int:did>',views.delcolor,name="delcolor"),
    path('colorupdate/<int:eid>',views.colorupdate,name="colorupdate"),


    #shop
    path('Shop/',views.Shop,name='Shop'),
    path('acceptshop/<int:aid>',views.acceptshop,name="acceptshop"),
    path('rejectedshop/<int:rid>',views.rejectedshop,name="rejectedshop"),
    path('acceptshoplist/',views.acceptshoplist,name='acceptshoplist'),
    path('rejectedshoplist/',views.rejectedshoplist,name='rejectedshoplist'),




    
    #center
    path('Center/',views.Center,name='Center'),
    path('acceptcenter/<int:aid>',views.acceptcenter,name="acceptcenter"),
    path('rejectedcenter/<int:rid>',views.rejectedcenter,name="rejectedcenter"),
    path('acceptcenterlist/',views.acceptcenterlist,name='acceptcenterlist'),
    path('rejectedcenterlist/',views.rejectedcenterlist,name='rejectedcenterlist'),




    #logout
    path('logout/',views.logout,name="logout")

]