from django.db import models

class NewSessionForm(models.Model):
    sessionNum = models.CharField(max_length=10)
    roomNum = models.CharField(max_length=10)
    
    project_name= models.CharField(max_length=20)
    group_name= models.CharField(max_length=20)
    advisor_name= models.CharField(max_length=20)
   
    def is_valid():
        return true;
