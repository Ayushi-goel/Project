from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import re
import mysql.connector


class Plants(models.Model):
    Name = models.CharField(max_length=100)
    Species_id= models.CharField(max_length=100,primary_key=True)
         
    def __str__(self):
    	 return self.Name
    

class Information(models.Model):
    Family=models.CharField(max_length=100)
    Scientific_Name=models.CharField(max_length=100)
    Synonym=models.CharField(max_length=100)
    Vernacular_name=models.CharField(max_length=100)
    Species = models.OneToOneField(Plants,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
    	 return self.Family

class Image(models.Model):
 Species  = models.ForeignKey(Plants,on_delete=models.CASCADE)
 image_name =models.CharField(max_length=100,primary_key=True)
 
   

# Create your models here.
