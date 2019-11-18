from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from manager.models import NewSessionForm, Group
from django.core.mail import EmailMessage


# Create your views here.

def admin(request):
    return render(request, 'admin.html')

def adminoptions(request):
    return render(request, 'adminoptions.html')

def adminforms(request):
    return render(request, 'adminforms.html')

def addgroupform(request):
    return render(request, 'addgroupform.html')

def sendscores(request):
    return render(request, 'sendscores.html')

def thankyouadmin(request):
    return render(request, 'thankyouadmin.html')

def edit_session(request, session_id):
    session = get_object_or_404(NewSessionForm, pk=session_id)
    return render(request, 'editsessionform.html', {'session': session})

def update_session(request, session_id):
    mysession = get_object_or_404(NewSessionForm, pk=session_id)
    mysession.sessionNum = request.POST['sessionNum']
    mysession.roomNum = request.POST['roomNum']
    mysession.save()

    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editsession.html', {'session_list': session_list} )

def delete_session(request, session_id):
    session = get_object_or_404(NewSessionForm, pk=session_id)
    session.delete()

    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editsession.html', {'session_list': session_list} )

def show_session(request, session_id):
    mysession = get_object_or_404(NewSessionForm, pk=session_id)
    group_list = Group.objects.order_by('group_name')
    return render(request, 'showsessiondetail.html', {'session': mysession, 'group_list': group_list} )

def add_group(request):
 
    # create a Group instance and populate it with data from the request form:
    mygroup = Group()

    mygroup.project_name= request.POST['project']
    mygroup.group_name= request.POST['group']
    mygroup.advisor_name= request.POST['advisor']
    session = get_object_or_404(NewSessionForm, pk=request.POST['session_id'])
    mygroup.session = session
    mygroup.save()

    session = get_object_or_404(NewSessionForm, pk=mygroup.session.id)
    group_list = Group.objects.order_by('project_name')
    return render(request, 'showsessiondetail.html', {'session': session, 'group_list': group_list} )

def edit_group(request, group_id):
    mygroup = get_object_or_404(Group, pk=group_id)
    return render(request, 'editgroupform.html', {'group': mygroup})

def update_group(request, group_id):
    mygroup = get_object_or_404(Group, pk=group_id)
    mygroup.project_name= request.POST['project']
    mygroup.group_name = request.POST['group']
    mygroup.advisor_name = request.POST['advisor']

    mygroup.save()

    session = get_object_or_404(NewSessionForm, pk=mygroup.session.id)
    group_list = Group.objects.order_by('project_name')
    return render(request, 'showsessiondetail.html', {'session': session, 'group_list': group_list} )


def delete_group(request, group_id):
    mygroup = get_object_or_404(Group, pk=group_id)
    mygroup.delete()

    session = get_object_or_404(NewSessionForm, pk=mygroup.session.id)
    group_list = Group.objects.order_by('project_name')
    return render(request, 'showsessiondetail.html', {'session': session, 'group_list': group_list} )

def editsession(request):
    session_list = NewSessionForm.objects.order_by('sessionNum')
    group_list = Group.objects.order_by('group_name')
    return render(request, 'editsession.html', {'session_list': session_list, 'group_list': group_list} )



def add_session(request):

    mysession = NewSessionForm()

     # process the data in form.cleaned_data as required
    mysession.sessionNum = request.POST['sessionNum']
    mysession.roomNum = request.POST['roomNum']

    mysession.save()


    # check whether it's valid:
    # if mysession.is_valid():

    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editsession.html', {'session_list': session_list})
    
def send_email(request):
    msg = EmailMessage(
		'Request Callback', 
		'Here is the message.',
		DEFAULT_FROM_EMAIL,
		['andresc98@gmail.com'],
	)
    msg.send()
    return HttpResponseRedirect('/')

