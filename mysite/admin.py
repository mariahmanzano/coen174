from django.contrib import admin
from manager.models import Group, NewSessionForm
from judges.models import PerGroupForm, PerSessionForm

admin.site.register(NewSessionForm)
admin.site.register(Group)
admin.site.register(PerGroupForm)
admin.site.register(PerSessionForm)
