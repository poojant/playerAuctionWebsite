from django.db import models

# Create your models here.
class PlayerList(models.Model):
	name = models.CharField(max_length=30, default='')
	role = models.CharField(max_length=50, default='')

class team1(models.Model):
	name = models.CharField(max_length=50, default='');

class PlayerImage(models.Model):
	img = models.FileField()