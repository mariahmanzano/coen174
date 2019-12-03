from django.db import models
from django import forms
import operator

# Collect information from Group Evaluation Form

class PerGroupForm(models.Model):
    
    CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )
    
    sessionNum = models.IntegerField()
    roomNum = models.IntegerField()
    
    project_name= models.CharField(max_length=20)
    group_name= models.CharField(max_length=20)
    advisor_name= models.CharField(max_length=20)
    
    technical_accuracy= models.IntegerField(choices=CHOICES)
    creativity= models.IntegerField(choices=CHOICES)
    supporting_work= models.IntegerField(choices=CHOICES)
    design_process= models.IntegerField(choices=CHOICES)
    project_complexity= models.IntegerField(choices=CHOICES)
    completion= models.IntegerField(choices=CHOICES)
    tests= models.IntegerField(choices=CHOICES)
    response= models.IntegerField(choices=CHOICES)
    organization= models.IntegerField(choices=CHOICES)
    time= models.IntegerField(choices=CHOICES)
    visual= models.IntegerField(choices=CHOICES)
    confidence= models.IntegerField(choices=CHOICES)
    
    overview= models.CharField(max_length=20)
    comments= models.CharField(max_length=100)
        
    def is_valid():
        return True;
        
# Collect information from Senior Design Experience Form
    
class PerSessionForm(models.Model):
    
    CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )
    
    dis1 = forms.CharField(max_length=20)
    
    q1= models.IntegerField(choices=CHOICES)
    q2= models.IntegerField(choices=CHOICES)
    q3= models.IntegerField(choices=CHOICES)
    q4= models.IntegerField(choices=CHOICES)
    q5= models.IntegerField(choices=CHOICES)
    q6= models.IntegerField(choices=CHOICES)
    q7= models.IntegerField(choices=CHOICES)
    q8= models.IntegerField(choices=CHOICES)
    q9= models.IntegerField(choices=CHOICES)
    q10= models.IntegerField(choices=CHOICES)
    q11= models.IntegerField(choices=CHOICES)
    q12= models.IntegerField(choices=CHOICES)
    
    comments= models.CharField(max_length=100)
    
    def is_valid():
        return True;


# Permissions for Judges to enter site

class judgePermissionModel(models.Model):
	judgePermissionModel = "Permission for judges."

	class Meta:
		permissions = [
			("is_judge", "This user is a judge")
		]

	def _str_(self):
		return self.judgePermissionModel
