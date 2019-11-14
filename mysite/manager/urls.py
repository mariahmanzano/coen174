"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# import views

urlpatterns = [
	# Path to Admin
	path('', views.admin, name='admin'),
	# Path to Admin Options
	path('adminoptions/', views.adminoptions, name='adminoptions'),
	# Path to Send Scores
	path('adminoptions/sendscores/', views.sendscores, name='sendscores'),
	# Path to Admin Forms
	path('adminoptions/adminforms/', views.add_session, name='adminforms'),
	
	# Path to add a new session
   	path('add_session/', views.add_session, name='addsession'),
	
	# Path to Thank You Admin
	path('adminoptions/sendscores/thankyouadmin/', views.thankyouadmin, name='thankyouadmin'),
	path('adminoptions/adminforms/thankyouadmin/', views.thankyouadmin, name='thankyouadmin'),
	
]
