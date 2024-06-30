from django.shortcuts import render,redirect
from Test.models import *

# Create your views here.
def loadinghomepage(request):
    return render(request,"Test/Homepage.html")



def teaminsertselect(request):
    data=tbl_team.objects.all()
    if request.method=="POST":
        tbl_team.objects.create(team_name=request.POST.get("txtname"),team_desc=request.POST.get("txtdesc"),team_photo=request.FILES.get("fileImage"))
        return redirect("Test:teaminsertselect")
    else:
        return render(request,"Test/Team.html",{"data":data})

def delteam(request,did):
    tbl_team.objects.get(id=did).delete()
    return redirect("Test:teaminsertselect")

def teamupdate(request,eid):
    data=tbl_team.objects.get(id=eid)
    if request.method=="POST":
        data.team_name=request.POST.get("txtname")
        data.team_desc=request.POST.get("txtdesc")
        data.save()
        return redirect("Test:teaminsertselect")
    else:
        return render(request,"Test\Team.html",{"editdata":data})   






def palyercategoryinsertselect(request):
    catdata=tbl_playercategory.objects.all()
    if request.method=="POST":
        cat=request.POST.get("txtcategory")
        tbl_playercategory.objects.create(pcategory_name=cat)
        return render(request,"Test/PlayerCategory.html",{'Data':catdata})
    else:
        return render(request,"Test/PlayerCategory.html",{'Data':catdata})
def delteamcat(request,did):
    tbl_playercategory.objects.get(id=did).delete()
    return redirect("Test:palyercategoryinsertselect")

def teamcatupdate(request,eid):
    data=tbl_playercategory.objects.get(id=eid)
    if request.method=="POST":
        data.pcategory_name=request.POST.get("txtcategory")
        data.save()
        return redirect("Test:palyercategoryinsertselect")
    else:
        return render(request,"Test\PlayerCategory.html",{"editdata":data})





def playerinsertselect(request):
    team = tbl_team.objects.all()
    playercategory = tbl_playercategory.objects.all()
    data=tbl_player.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        team = tbl_team.objects.get(id=request.POST.get('sel_team'))
        pcat = tbl_playercategory.objects.get(id=request.POST.get('sel_cat'))
        fileImage=request.FILES.get("fileImage")
        tbl_player.objects.create(team=team,playercategory=pcat,player_name=name,player_photo=fileImage)
        return render(request,"Test/Player.html",{'data':data})
    else:
        return render(request,"Test/Player.html",{'data':data,"catdata":playercategory,"teamdata":team})





def matchInsertSelect(request):
    team = tbl_team.objects.all()
    data = tbl_matchshedule.objects.all()
    if request.method=="POST":
        matchName=request.POST.get('txt_tname')
        team1 = tbl_team.objects.get(id=request.POST.get('sel_team1'))
        team2 = tbl_team.objects.get(id=request.POST.get('sel_team2'))
        fromdate=request.POST.get('txt_fdate')
        todate=request.POST.get('txt_tdate')
        venue=request.POST.get('txt_venue')
        tbl_matchshedule.objects.create(match_name=matchName,from_Date=fromdate,to_Date=todate,venue=venue,team=team1,team2=team2)
        return redirect("Test:matchInsertSelect")
    else:
        return render(request,"Test/Schedule.html",{'data':data,"teamdata":team})



def Playereleven(request):
    team = tbl_team.objects.all()
    player=tbl_player.objects.all()
    schedule=tbl_matchshedule.objects.all()
    data = tbl_playereleven.objects.all()
    if request.method=="POST":
        player = tbl_player.objects.get(id=request.POST.get('sel_player'))
        schedule=tbl_matchshedule.objects.get(id=request.POST.get('sel_schedule'))
        tbl_playereleven.objects.create(player=player,schedule=schedule)
        return redirect("Test:Playereleven")
    else:
        return render(request,"Test/PlayersEleven.html",{'data':data,"sdata":schedule,"teamdata":team})






def ajaxplayer(request):
    team = tbl_team.objects.get(id=request.GET.get("did"))
    player = tbl_player.objects.filter(team=team)
    return render(request,"Test/AjaxPlayer.html",{"playerdata":player})