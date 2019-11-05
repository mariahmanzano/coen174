from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def admin(request):
	return render(request, 'admin.html')

def judge(request):
	return render(request, 'judge.html')

def adminoptions(request):
	return render(request, 'adminoptions.html')

def judgeforms(request):
	return render(request, 'judgeforms.html')

def sendscores(request):
	return render(request, 'sendscores.html')

def persession(request):
	return render(request, 'perSession.html')

def adminforms(request):
	return render(request, 'adminforms.html')

def pergroup(request):
	return render(request, 'perGroup.html')

def thankyouadmin(request):
	return render(request, 'thankyouadmin.html')

def thankyou(request):
	return render(request, 'thankyou.html')

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NewSessionForm
from .models import NewSessionForm

def get_session(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NewSessionForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			sessionNum = form.cleaned_data['sessionNum']
			roomNum = form.cleaned_data['roomNum']

			project_name= form.cleaned_data['project']
			group_name= form.cleaned_data['group']
			advisor_name= form.cleaned_data['advisor']

			form.save()
			# redirect to a new URL:
			return HttpResponseRedirect('/thankyouadmin/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NewSessionForm()
		
	return render(request, 'adminforms.html', {'form': form})


from .forms import PerGroupForm
from .models import PerGroupForm

def get_pergroup(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PerGroupForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			sessionNum = form.cleaned_data['sessionNum']
			roomNum = form.cleaned_data['roomNum']

			project_name= form.cleaned_data['project']
			group_name= form.cleaned_data['group']
			advisor_name= form.cleaned_data['advisor']

			technical_accuracy= form.cleaned_data['design1']
			creativity= form.cleaned_data['design2']
			supporting_work= form.cleaned_data['design3']
			design_process= form.cleaned_data['design4']
			project_complexity= form.cleaned_data['design5']
			completion= form.cleaned_data['design6']
			tests= form.cleaned_data['design7']
			response= form.cleaned_data['design8']
			organization= form.cleaned_data['pres1']
			time= form.cleaned_data['pres2']
			visual= form.cleaned_data['pres3']
			confidence= form.cleaned_data['pres4']

			overview= form.cleaned_data['topics']
			comments= form.cleaned_data['comments']

			form.save()
			# redirect to a new URL:
			return HttpResponseRedirect('/thankyou/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form =PerGroupForm()
		
	return render(request, 'perGroup.html', {'form': form})


from .forms import PerSessionForm
from .models import PerSessionForm

def get_persession(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PerSessionForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			dis1= form.cleaned_data['dis1']
			q1= form.cleaned_data['q1']
			q2= form.cleaned_data['q2']
			q3= form.cleaned_data['q3']
			q4= form.cleaned_data['q4']
			q5= form.cleaned_data['q5']
			q6= form.cleaned_data['q6']
			q7= form.cleaned_data['q7']
			q8= form.cleaned_data['q8']
			q9= form.cleaned_data['q9']
			q10= form.cleaned_data['q10']
			q11= form.cleaned_data['q11']
			q12= form.cleaned_data['q12']

			comments= form.cleaned_data['comments']

			form.save()
			# redirect to a new URL:
			return HttpResponseRedirect('/thankyou/')

    # if a GET (or any other method) we'll create a blank form
'''else:
        form = PerSessionForm()
        return render(request, 'perSession.html', {'form': form})
'''
