from django.urls import path,include
from Test import views
app_name="Test"
urlpatterns = [

    path('Homepage/',views.loadinghomepage,name='loadinghomepage'),

    path('teaminsertselect/',views.teaminsertselect,name="teaminsertselect"),
    path('delteam/<int:did>',views.delteam,name="delteam"),
    path('teamupdate/<int:eid>',views.teamupdate,name="teamupdate"),


    path('palyercategoryinsertselect/',views.palyercategoryinsertselect,name="palyercategoryinsertselect"),
    path('delteamcat/<int:did>',views.delteamcat,name="delteamcat"),
    path('teamcatupdate/<int:eid>',views.teamcatupdate,name="teamcatupdate"),


    path('playerinsertselect/',views.playerinsertselect,name="playerinsertselect"),



    path('Shedule/',views.matchInsertSelect,name="matchInsertSelect"),



    path('Playereleven/',views.Playereleven,name="Playereleven"),
    path('AjaxPlace/',views.ajaxplayer,name="ajaxplayer"),


]