from django.db import models

# Create your models here.

class Employee(models.Model):
	EmpName = models.CharField(max_length=30)
	EmpId = models.IntegerField()
	Desg = models.CharField(max_length=30)
	Doj = models.DateField()
	Dep = models.CharField(max_length=30)
	Sal = models.FloatField()
	Exp = models.IntegerField()