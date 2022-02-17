from django.contrib import admin

from viewsetclasses.models import Patient, Drug, DrugCategory

admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(DrugCategory)
