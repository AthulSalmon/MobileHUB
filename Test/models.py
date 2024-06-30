from django.db import models


# Create your models here.
class tbl_team(models.Model):
    team_name=models.CharField(max_length=50)
    team_desc=models.CharField(max_length=50)
    team_photo = models.FileField(upload_to='Assets/TeamPhoto/')


class tbl_playercategory(models.Model):
    pcategory_name = models.CharField(max_length=50)


class tbl_player(models.Model):
    team = models.ForeignKey(tbl_team, on_delete=models.CASCADE)
    playercategory = models.ForeignKey(tbl_playercategory, on_delete=models.CASCADE)
    player_name=models.CharField(max_length=50)
    player_photo = models.FileField(upload_to='Assets/PlayerPhoto/')



class tbl_matchshedule(models.Model):
    match_name=models.CharField(max_length=50)
    from_Date=models.CharField(max_length=50)
    to_Date=models.CharField(max_length=50)
    venue=models.CharField(max_length=50)
    team = models.ForeignKey(tbl_team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(tbl_team, on_delete=models.CASCADE, related_name='team2_matches')



class tbl_playereleven(models.Model):
    player = models.ForeignKey(tbl_player, on_delete=models.CASCADE)
    schedule = models.ForeignKey(tbl_matchshedule, on_delete=models.CASCADE)
