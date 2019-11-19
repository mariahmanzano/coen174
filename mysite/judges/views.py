from django.shortcuts import render
from django import forms
from manager.models import NewSessionForm, Group
from django.http import HttpResponseRedirect
from judges.models import PerGroupForm

# Create your views here.

def judge(request):
    return render(request, 'judge.html')

def judgeforms(request):
    return render(request, 'judgeforms.html')

def persession(request):
    return render(request, 'perSession.html')

def pergroup(request):
        session_list = NewSessionForm.objects.order_by('sessionNum')
        group_list = Group.objects.order_by('project_name')
        return render(request, 'perGroup.html', {'session_list': session_list, 'group_list': group_list})

def thankyou(request):
    return render(request, 'thankyou.html')

from django.http import HttpResponseRedirect
from django.shortcuts import render

from judges.models import PerGroupForm
from manager.models import NewSessionForm

def get_pergroup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        mygroup = PerGroupForm()
        
	# process the data in form.cleaned_data as required
        mygroup.sessionNum = request.POST['sessionId']
        mygroup.project_name= request.POST['group.project_name']
	
        #mygroup.group_name= request.POST['group']
        #mygroup.advisor_name= request.POST['advisor']

        mygroup.technical_accuracy= request.POST['design1']
        mygroup.creativity= request.POST['design2']
        mygroup.supporting_work= request.POST['design3']
        mygroup.design_process= request.POST['design4']
        mygroup.project_complexity= request.POST['design5']
        mygroup.completion= request.POST['design6']
        mygroup.tests= request.POST['design7']
        mygroup.response= request.POST['design8']
        mygroup.organization= request.POST['pres1']
        mygroup.time= request.POST['pres2']
        mygroup.visual= request.POST['pres3']
        mygroup.confidence= request.POST['pres4']

        mygroup.overview= request.POST['topics']
        mygroup.comments= request.POST['comments']

        
        # check whether it's valid:
        #if mygroup.is_valid():

        mygroup.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/thankyou/')
        return render(request, 'perGroup.html')


from judges.models import PerSessionForm

def get_persession(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        mysession = PerSessionForm()
        
        # process the data in form.cleaned_data as required
        mysession.dis1= request.POST['dis1']
        mysession.q1= request.POST['q1']
        mysession.q2= request.POST['q2']
        mysession.q3= request.POST['q3']
        mysession.q4= request.POST['q4']
        mysession.q5= request.POST['q5']
        mysession.q6= request.POST['q6']
        mysession.q7= request.POST['q7']
        mysession.q8= request.POST['q8']
        mysession.q9= request.POST['q9']
        mysession.q10= request.POST['q10']
        mysession.q11= request.POST['q11']
        mysession.q12= request.POST['q12']

        mysession.comments= request.POST['comments']
        
        # check whether it's valid:
        #if mysession.is_valid():

        mysession.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/thankyou/')
        return render(request, 'perSession.html')
