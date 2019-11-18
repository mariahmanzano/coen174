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
	path('adminoptions/adminforms/', views.adminforms, name='adminforms'),
	
	# Path from the session form to add the session
	path('adminoptions/addsession/', views.add_session, name='addsession'),
	# Path to edit a session
	path('edit_session/<int:session_id>/', views.edit_session, name='editasession'),

	# Path to delete a session
	path('delete_session/<int:session_id>/', views.delete_session, name='deletesession'),

	# Path to update a session
	path('update_session/<int:session_id>/', views.update_session, name='updatesession'),

	# Path to display session details
	path('show_session/<int:session_id>/', views.show_session, name='showsession'),

	# Path to add a new group
   	path('add_group_form/<int:session_id>/', views.addgroupform, name='addgroupform'),

	# Path to add a new group
   	path('add_group/<int:session_id>/', views.add_group, name='addgroup'),

	# Path to edit a group
	path('edit_group/<int:group_id>/', views.edit_group, name='editgroup'),

	# Path to delete a group
	path('delete_group/<int:group_id>/', views.delete_group, name='deletegroup'),

	# Path to update a group
	path('update_group/<int:group_id>/', views.update_group, name='updategroup'),

	# Path to edit a session
	path('adminoptions/editsession/', views.editsession, name='editsession'),

	# Path to Thank You Admin
	path('adminoptions/sendscores/thankyouadmin/', views.thankyouadmin, name='thankyouadmin'),
	path('adminoptions/adminforms/thankyouadmin/', views.thankyouadmin, name='thankyouadmin'),
 
    # Path to View Results
    path('results/', views.display_results, name='results'),
]
