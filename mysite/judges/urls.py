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
	
	# Path to Judge
	path('', views.judge, name='judge'),
	# Path to Judge Forms
	path('judgeforms/', views.judgeforms, name='judgeforms'),
	# Path to Per Session Forms
	path('judgeforms/persession/', views.persession, name='persession'),
	# Path to Per Group Forms
	path('judgeforms/pergroup/', views.pergroup, name='pergroup'),
	# Path to Thank You Judges
	path('judgeforms/persession/thankyou/', views.thankyou, name='thankyou'),
	path('judgeforms/pergroup/thankyou/', views.thankyou, name='thankyou')
	
]

