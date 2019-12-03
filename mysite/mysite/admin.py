#Sets up the root url, which begins with '/home/'
#Adds the models from manager and judges, and registers them to the root

from django.contrib import admin
from manager.models import Group, NewSessionForm
from judges.models import PerGroupForm, PerSessionForm

admin.site.register(NewSessionForm)
admin.site.register(Group)
admin.site.register(PerGroupForm)
admin.site.register(PerSessionForm)
admin.site.site_url = '/home/'
