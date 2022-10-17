from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ['rname','rsubject','message']

    

admin.site.register(Report,ReportAdmin)

