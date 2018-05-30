# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    pass

class Pet(models.Model):
    pet = models.IntegerField(primary_key=True)
    user_list = models.ForeignKey(User)

class Pet_State(models.Model):
     pet_id = models.ForeignKey(Pet)
     pet_clean = models.IntegerField()
     pet_hunger = models.IntegerField() 

class Goods_table(models.Model):
    user_info = models.ForeignKey(User)
    cookies = models.BooleanField() 
    soap = models.BooleanField()
