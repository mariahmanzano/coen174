from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from manager.models import NewSessionForm, Group
from judges.models import PerSessionForm, PerGroupForm
from django.core.mail import EmailMessage
import operator


# Admin side views. Define and return rendered admin pages. Define admin side functions.

#return admin.html
def admin(request):
    return render(request, 'admin.html')

#return adminoptions.html
def adminoptions(request):
    return render(request, 'adminoptions.html')

#return adminforms.html
def adminforms(request):
    return render(request, 'adminforms.html')

#return addgroupform.html
#lets admin users create groups with session_id parameter
def addgroupform(request, session_id):
    return render(request, 'addgroupform.html', {'session_id': session_id})

#return sendscores.html
def sendscores(request):
    return render(request, 'sendscores.html')

#return thankyouadmin.htmll
def thankyouadmin(request):
    return render(request, 'thankyouadmin.html')
  
#return results.html
#displays list of sessions with corresponding groups and averaged scores using session_list
def results(request):
	session_list = NewSessionForm.objects.order_by('sessionNum')
	return render(request, 'results.html', {'session_list': session_list})

#returns editsessionform.html
#form to enter new session information using session_id key
def edit_session(request, session_id):
    session = get_object_or_404(NewSessionForm, pk=session_id)
    return render(request, 'editsessionform.html', {'session': session})

#returns editsession.html
#process data from new session form (input session and room number)
#displays session_list
def update_session(request, session_id):
    mysession = get_object_or_404(NewSessionForm, pk=session_id)
    mysession.sessionNum = request.POST['sessionNum']
    mysession.roomNum = request.POST['roomNum']
    mysession.save()

    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editsession.html', {'session_list': session_list} )

#return editsession.html
#lets admin users delete sessions using session_id key
#displays session_list minus deleted session
def delete_session(request, session_id):
    session = get_object_or_404(NewSessionForm, pk=session_id)
    session.delete()

    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editsession.html', {'session_list': session_list} )

#returns showsessiondetail.html
#displays list group_list of groups within a session using session_id key
def show_session(request, session_id):
    mysession = get_object_or_404(NewSessionForm, pk=session_id)
    group_list = Group.objects.order_by('group_name')
    return render(request, 'showsessiondetail.html', {'session': mysession, 'group_list': group_list} )

#returns showsessiondetail.html
#lets admin users create new groups in a session using session_id key
#uses project, group, and advisor inputs
#display group_list with newly created group
def add_group(request, session_id):

    mygroup = Group()

    mygroup.project_name= request.POST['project']
    mygroup.group_name= request.POST['group']
    mygroup.advisor_name= request.POST['advisor']
    session = get_object_or_404(NewSessionForm, pk=session_id)
    mygroup.session = session
    mygroup.save()

    group_list = Group.objects.order_by('project_name')
    return render(request, 'showsessiondetail.html', {'session': session, 'group_list': group_list} )

#returns editgroupform.html
#form to create new group in a session by inputting project name, group name, advisor name
def edit_group(request, group_id):
    mygroup = get_object_or_404(Group, pk=group_id)
    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editgroupform.html', {'group': mygroup, 'session_list': session_list})

#returns showsessiondetail.html
#process data from new group form (project, group, advisor)
def update_group(request, group_id):
    mygroup = get_object_or_404(Group, pk=group_id)
    mygroup.project_name= request.POST['project']
    mygroup.group_name = request.POST['group']
    mygroup.advisor_name = request.POST['advisor']
    session = get_object_or_404(NewSessionForm, pk=request.POST['sessionId'])
    mygroup.session = session
    mygroup.save()

    group_list = Group.objects.order_by('project_name')
    return render(request, 'showsessiondetail.html', {'session': session, 'group_list': group_list} )

#returns showsessiondetail.html
#lets admin users delete group from a session given session_id
def delete_group(request, group_id):
    mygroup = get_object_or_404(Group, pk=group_id)
    mygroup.delete()

    session = get_object_or_404(NewSessionForm, pk=mygroup.session.id)
    group_list = Group.objects.order_by('project_name')
    return render(request, 'showsessiondetail.html', {'session': session, 'group_list': group_list} )

#returns editsession.html
#displays lists of groups and sessions
def editsession(request):
    session_list = NewSessionForm.objects.order_by('sessionNum')
    group_list = Group.objects.order_by('group_name')
    return render(request, 'editsession.html', {'session_list': session_list, 'group_list': group_list} )

#returns editsession.html
#process data from new session form (session and room number)
def add_session(request):

    mysession = NewSessionForm()

    mysession.sessionNum = request.POST['sessionNum']
    mysession.roomNum = request.POST['roomNum']

    mysession.save()

    session_list = NewSessionForm.objects.order_by('sessionNum')
    return render(request, 'editsession.html', {'session_list': session_list})

#returns results.html
#calculates average score from submitted experience evaluation forms
#calculates average score for each group in a session from project evaluation forms
#displays average scores in table
def display_results(request):

	# Senior Design Experience

    all_forms = PerSessionForm.objects.all()

	# Average

    session_sum = 0
    num_sessions= 0
    session_eval_average= 0
    for form in all_forms:
        session_sum += (form.q1 + form.q2 + form.q3 + form.q4 + form.q5 + form.q6 + form.q7 + form.q8 + form.q9 + form.q10 + form.q11 + form.q12)
        num_sessions += 1

    if num_sessions > 0:
        session_eval_average = '%.2f'%(session_sum / num_sessions)
    
    # Project Evaluation Form
    
    eval_forms = PerGroupForm.objects.all()
    

    # Average
    
    # Create a project evaluation list, one entry for each group.
    # Each entry is a tuple of 3 values: session number, project name, and average evaluation score for the project.
    
    eval_sum = 0
    eval_total = 12

    eval_projects = []
    for form in eval_forms:
        eval_sum = (form.technical_accuracy + form.creativity + form.supporting_work + form.design_process + form.project_complexity + form.completion + form.tests + form.response + form.organization + form.time + form.visual + form.confidence)
        avg = '%.2f'%(eval_sum / eval_total)
        group_eval = [form.sessionNum, form.project_name, form.group_name, form.advisor_name, avg] # the values order must match the column order
        eval_projects.append(group_eval)
    
    eval_projects = sorted(eval_projects, key = operator.itemgetter(0, 4))
    
    return render(request, 'results.html', {'average': session_eval_average, 'eval_projects': eval_projects})
    
 
