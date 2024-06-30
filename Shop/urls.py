from django.urls import path,include
from Shop import views
app_name="Shop"
urlpatterns = [

    path('homepage/',views.homepage,name='homepage'),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    

#product
path('productinsertselect/',views.productinsertselect,name="productinsertselect"),
path('delproduct/<int:did>',views.delproduct,name="delproduct"),
path('productupdate/<int:eid>',views.productupdate,name="productupdate"),
path('Ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),


#stock
path('Addstock/<int:did>', views.addstock,name="addstock"),
path('delstock/<int:did>', views.delstock,name="delstock"),



path('vieworder/',views.vieworder,name="vieworder"),
path('details/<int:did>',views.details,name="details"),
path('updateproductbooking/<int:bid>',views.updateproductbooking,name="updateproductbooking"),




#logout
    path('logout/',views.logout,name="logout"),

    path('BookingReport/',views.BookingReport,name='BookingReport'),
    path('viewmore/<int:did>',views.viewmore,name="viewmore"),


]