from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.CharField(max_length=127, null=False, blank=True)
    game_name = models.CharField(default="Unnamed Game", max_length=32, null=False, blank=False)
    game_status = models.CharField(default="open", max_length=10, choices=(("open","open"),("over","over"),("left","left")))
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastmodify_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    player_11 = models.CharField(max_length=32, null=False, blank=True)
    player_11_image = models.URLField(max_length=300, null=False, blank=True)
    player_12 = models.CharField(max_length=32, null=False, blank=True)
    player_12_image = models.URLField(max_length=300, null=False, blank=True)
    player_13 = models.CharField(max_length=32, null=False, blank=True)
    player_13_image = models.URLField(max_length=300, null=False, blank=True)
    player_21 = models.CharField(max_length=32, null=False, blank=True)
    player_21_image = models.URLField(max_length=300, null=False, blank=True)
    player_22 = models.CharField(max_length=32, null=False, blank=True)
    player_22_image = models.URLField(max_length=300, null=False, blank=True)
    player_23 = models.CharField(max_length=32, null=False, blank=True)
    player_23_image = models.URLField(max_length=300, null=False, blank=True)
    log =  models.TextField(blank=True)
    player_11_hand =  models.TextField(blank=True)
    player_12_hand =  models.TextField(blank=True)
    player_13_hand =  models.TextField(blank=True)
    player_21_hand =  models.TextField(blank=True)
    player_22_hand =  models.TextField(blank=True)
    player_23_hand =  models.TextField(blank=True)
    team_1_status = models.CharField(max_length=40, null=False, blank=True)
    team_2_status = models.CharField(max_length=40, null=False, blank=True)
