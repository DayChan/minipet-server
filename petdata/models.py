# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    pass

class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
    pet_name = models.CharField(max_length = 100)
    user_list = models.ForeignKey(User)

class Pet_State(models.Model):
    id = models.IntegerField(primary_key=True)
    pet_id = models.ForeignKey(Pet)
    pet_clean = models.IntegerField()
    pet_hunger = models.IntegerField() 

class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    user_info = models.ForeignKey(User)
    cookies = models.BooleanField() 
    soap = models.BooleanField()
