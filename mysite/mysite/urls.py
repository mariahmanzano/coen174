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
from django.urls import path
from . import views
# import views

urlpatterns = [
	path('admin/', admin.site.urls),
	# Path to Index
	path('home/', views.home, name='home'),

	# Path to Admin
	path('home/admin/', views.admin, name='admin'),
	# Path to Admin Options
	path('home/admin/adminoptions/', views.adminoptions, name='adminoptions'),
	# Path to Send Scores
	path('home/admin/adminoptions/sendscores/', views.sendscores, name='sendscores'),
	# Path to Admin Forms
	path('home/admin/adminoptions/adminforms/', views.adminforms, name='adminforms'),
	# Path to Thank You Admin
	path('home/admin/adminoptions/sendscores/thankyouadmin/', views.thankyouadmin, name='thankyouadmin'),
	path('home/admin/adminoptions/adminforms/thankyouadmin/', views.thankyouadmin, name='thankyouadmin'),

	# Path to Judge
	path('home/judge/', views.judge, name='judge'),
	# Path to Judge Forms
	path('home/judge/judgeforms/', views.judgeforms, name='judgeforms'),
	# Path to Per Session Forms
	path('home/judge/judgeforms/persession/', views.persession, name='persession'),
	# Path to Per Group Forms
	path('home/judge/judgeforms/pergroup/', views.pergroup, name='pergroup'),
	# Path to Thank You Judges
	path('home/judge/judgeforms/persession/thankyou/', views.thankyou, name='thankyou'),
	path('home/judge/judgeforms/pergroup/thankyou/', views.thankyou, name='thankyou')
]

