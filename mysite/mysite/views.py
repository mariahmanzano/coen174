from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def admin(request):
	return render(request, 'admin.html')
