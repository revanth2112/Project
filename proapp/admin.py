from django.contrib import admin
from proapp.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	list_display=['EmpName','EmpId','Desg','Doj','Dep','Sal','Exp']

admin.site.register(Employee,EmployeeAdmin)