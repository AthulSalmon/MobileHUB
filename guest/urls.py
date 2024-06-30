from django.urls import path
from guest import views
app_name="guest"
urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    

    path('Login/',views.Login,name="Login"),



    path('',views.loadingpage,name="loadingpage"),

    path('ShopRegistration/',views.ShopRegistration,name="ShopRegistration"),
    


     path('ServicecenterRegistration/',views.ServicecenterRegistration,name="ServicecenterRegistration"),



     path('Otpverify/',views.Otpverify,name="Otpverify"),
]