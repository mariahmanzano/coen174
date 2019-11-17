from django.shortcuts import render
from django import forms

# Create your views here.

def admin(request):
    return render(request, 'admin.html')

def adminoptions(request):
    return render(request, 'adminoptions.html')

def adminforms(request):
    return render(request, 'adminforms.html')

def sendscores(request):
    return render(request, 'sendscores.html')
    
def thankyouadmin(request):
    return render(request, 'thankyouadmin.html')

def editsession(request):
	session_list = NewSessionForm.objects.order_by('sessionNum')[:5]
	return render(request, 'editsession.html', {'session_list': session_list} )
    
from django.http import HttpResponseRedirect
from django.shortcuts import render

from manager.models import NewSessionForm

def add_session(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        mysession = NewSessionForm()
        
         # process the data in form.cleaned_data as required
        mysession.sessionNum = request.POST['sessionNum']
        mysession.roomNum = request.POST['roomNum']
        mysession.project_name= request.POST['project']

        # TODO: could be more than one group in the session, create a loop
        mysession.group_name= request.POST['group']
        mysession.advisor_name= request.POST['advisor']

        # check whether it's valid:
		# if mysession.is_valid():
            
        mysession.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/home/admin/adminoptions/adminforms/thankyouadmin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        mysession = NewSessionForm()
        
    return render(request, 'adminforms.html')
