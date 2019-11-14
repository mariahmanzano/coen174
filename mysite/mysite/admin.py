from django.contrib import admin
from judges.models import NewSessionForm, PerGroupForm, PerSessionForm

admin.site.register(NewSessionForm)
admin.site.register(PerGroupForm)
admin.site.register(PerSessionForm)
