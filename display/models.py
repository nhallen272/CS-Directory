from ast import BinOp
from django.db import models


class ResearchCategory(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class FacultyModel(models.Model):           
    name = models.CharField(max_length=100, default=' ')               # name
    title = models.CharField(max_length=40, default=' ')               # job title
    email = models.CharField(max_length=60, default=' ')               # email
    phone = models.CharField(max_length=15, default=' ')               # phone 
    pic = models.ImageField(upload_to='images/', null=True, blank=True, default="images/default_profile.png") 
    address = models.TextField(default=' ', null=True)
    website = models.URLField(null=True)                                # link to their .cs.odu.edu website
    researchTypes = models.ManyToManyField('ResearchCategory')          # research types
    bio = models.TextField(default=' ', null=True)                      # personal biography, research, etc.                                                             
    edited = models.BooleanField(default=False, null=True)              # whether it has been edited by the faculty
    
    def __str__(self):
        return self.name