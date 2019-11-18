from django import forms 

class NewSessionForm(forms.Form):
	post = forms.CharField()
