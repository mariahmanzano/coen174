from django import forms

class NewSessionForm(forms.Form):
    sessionNum = forms.CharField(min_length=1)
    roomNum = forms.CharField(min_length=1)
    
    project_name= forms.CharField()
    group_name= forms.CharField()
    advisor_name= forms.CharField()
  

class PerGroupForm(forms.Form):
    sessionNum = forms.IntegerField()
    roomNum = forms.IntegerField()
    
    project_name= forms.ChoiceField()
    group_name= forms.ChoiceField()
    advisor_name= forms.ChoiceField()
    
    technical_accuracy= forms.IntegerField()
    creativity= forms.IntegerField()
    supporting_work= forms.IntegerField()
    design_process= forms.IntegerField()
    project_complexity= forms.IntegerField()
    completion= forms.IntegerField()
    tests= forms.IntegerField()
    response= forms.IntegerField()
    organization= forms.IntegerField()
    time= forms.IntegerField()
    visual= forms.IntegerField()
    confidence= forms.IntegerField()
    
    overview= forms.ChoiceField()
    comments= forms.CharField()
    
    
    
class PerSessionForm(forms.Form):
    discipline= forms.ChoiceField()
    
    q1= forms.IntegerField()
    q2= forms.IntegerField()
    q3= forms.IntegerField()
    q4= forms.IntegerField()
    q5= forms.IntegerField()
    q6= forms.IntegerField()
    q7= forms.IntegerField()
    q8= forms.IntegerField()
    q9= forms.IntegerField()
    q10= forms.IntegerField()
    q11= forms.IntegerField()
    q12= forms.IntegerField()
    
    comments= forms.CharField()
    
    

