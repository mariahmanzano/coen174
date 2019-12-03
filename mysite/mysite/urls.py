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
from django.contrib.auth import login, logout
# import views
# Provides the start path for admin and judge
urlpatterns = [
	path('admin/', admin.site.urls),

	# Path to Index
	path('home/', views.home, name='home'),

	# Path to Login
	path('accounts/', include('django.contrib.auth.urls')),

	# Path to Admin
	path('home/admin/', include('manager.urls')), 

	# Path to Judge
	path('home/judge/', include('judges.urls')),
]
