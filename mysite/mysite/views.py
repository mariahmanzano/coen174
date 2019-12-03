from django.shortcuts import render
from django import forms


# Create your views here.

# Takes the web request and returns a render of the 'index.html'
def home(request):
    return render(request, 'index.html')
