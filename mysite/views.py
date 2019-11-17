from django.shortcuts import render
from django import forms


# Create your views here.

def home(request):
    return render(request, 'index.html')
