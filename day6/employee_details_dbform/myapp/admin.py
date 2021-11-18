from django.contrib import admin
from .models import Employee
# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddress', 'eemail']
admin.site.register(Employee,Employeeadmin)