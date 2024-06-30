from django.urls import path
from user import views
app_name="user"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),


    path('complaint/',views.POSTComplaint,name="POSTComplaint"),
    path('complaintDelete/<int:did>',views.complaintDelete,name="complaintDelete"),
    

    path('ServiceBooking/',views.servicebooking,name="servicebooking"),
    path('search/',views.search,name="search"),


    path('productbooking/',views.productbooking,name="productbooking"),
    path('productbook/<int:did>',views.productbook,name="productbook"),
    path('Mycart/',views.Mycart,name="mycart"),
    path('DelCart/<int:did>',views.DelCart,name="delcart"),
    path('CartQty/',views.CartQty,name="cartqty"),
    path('Payment/',views.payment,name="payment"),
    path('productsearch/',views.productsearch,name="productsearch"),
    path('Billing/<int:did>',views.Billing,name="Billing"),
    path('viewmore/<int:vid>',views.viewmore,name="viewmore"),
    path('viewproduct',views.viewproduct,name="viewproduct"),



    path('Myorder/',views.myorder,name="myorder"),
    #path('details/<int:did>',views.details,name="details"),
    path('cancel/<int:cid>',views.cancel,name="cancel"),
    path('mybooking/',views.mybooking,name="mybooking"),



    
    path('rating/<str:cid>',views.rating,name="rating"),
    path('ajaxrating',views.ajaxrating,name="ajaxrating"),
    path('starrating/',views.starrating,name="starrating"),



    path('appointment/<int:aid>',views.appointment,name="appointment"),


    path('servicerating/<str:cid>',views.servicerating,name="servicerating"),
    path('ajaxservicerating',views.ajaxservicerating,name="ajaxservicerating"),
    path('starservicerating/',views.starservicerating,name="starservicerating"),


#logout
    path('logout/',views.logout,name="logout")
]