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
	return render(request, 'persession.html')

def adminforms(request):
	return render(request, 'adminforms.html')

def pergroup(request):
	return render(request, 'pergroup.html')

def thankyouadmin(request):
	return render(request, 'thankyouadmin.html')

def thankyou(request):
	return render(request, 'thankyou.html')
