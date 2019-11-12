from django import forms
from django.forms import ModelForm
from django.db import models

class NewSessionForm(models.Model):
    sessionNum = models.CharField(max_length=10)
    roomNum = models.CharField(max_length=10)
    
    project_name= models.CharField(max_length=20)
    group_name= models.CharField(max_length=20)
    advisor_name= models.CharField(max_length=20)
  

class PerGroupForm(models.Model):
    sessionNum = models.IntegerField()
    roomNum = models.IntegerField()
    
    project_name= models.CharField(max_length=20)
    group_name= models.CharField(max_length=20)
    advisor_name= models.CharField(max_length=20)
    
    technical_accuracy= models.IntegerField()
    creativity= models.IntegerField()
    supporting_work= models.IntegerField()
    design_process= models.IntegerField()
    project_complexity= models.IntegerField()
    completion= models.IntegerField()
    tests= models.IntegerField()
    response= models.IntegerField()
    organization= models.IntegerField()
    time= models.IntegerField()
    visual= models.IntegerField()
    confidence= models.IntegerField()
    
    overview= models.CharField(max_length=20)
    comments= models.CharField(max_length=100)
    
    
    
class PerSessionForm(models.Model):
    discipline= forms.CharField(max_length=20)
    
    q1= models.IntegerField()
    q2= models.IntegerField()
    q3= models.IntegerField()
    q4= models.IntegerField()
    q5= models.IntegerField()
    q6= models.IntegerField()
    q7= models.IntegerField()
    q8= models.IntegerField()
    q9= models.IntegerField()
    q10= models.IntegerField()
    q11= models.IntegerField()
    q12= models.IntegerField()
    
    comments= models.CharField(max_length=100)
