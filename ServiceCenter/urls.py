from django.urls import path,include
from ServiceCenter import views
app_name="ServiceCenter"
urlpatterns = [

    
path('homepage/',views.homepage,name='homepage'),

path('My_profile/',views.my_pro,name="my_pro"),
path('editprofile/',views.editprofile,name="editprofile"),
path('changepassword/',views.changepassword,name="changepassword"),

#service
path('serviceinsertselect/',views.serviceinsertselect,name="serviceinsertselect"),
path('delservice/<int:did>',views.delservice,name="delservice"),
path('serviceupdate/<int:eid>',views.serviceupdate,name="serviceupdate"),


path('vieworder/',views.vieworder,name="vieworder"),
path('acceptbooking/<int:aid>',views.acceptbooking,name="acceptbooking"),
path('rejectedbooking/<int:rid>',views.rejectedbooking,name="rejectedbooking"),
path('acceptedlist/',views.acceptedlist,name="acceptedlist"),
path('rejectedlist/',views.rejectedlist,name="rejectedlist"),

#logout
    path('logout/',views.logout,name="logout"),

]