from django.contrib import admin
from manager.models import NewSessionForm
from judges.models import PerGroupForm, PerSessionForm

admin.site.register(NewSessionForm)
admin.site.register(PerGroupForm)
admin.site.register(PerSessionForm)
