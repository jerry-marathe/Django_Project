from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','eemail','econtact']

admin.site.register(Employee,EmployeeAdmin)