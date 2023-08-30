from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from proapp.models import Employee
from proapp.forms import EmployeeForm
from proapp.forms import SignUpForm

# Create your views here.

def home(request):
	return render(request,'proapp/home.html')

@login_required
def hr(request):
	return render(request,'proapp/hr.html')

def emp(request):
	return render(request,'proapp/employee.html')

@login_required
def emp_form(request):
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/empdata')
	return render(request,'proapp/empform.html',{'form':form})

@login_required
def emps(request):
	employees=Employee.objects.all()
	return render(request,'proapp/empdata.html',{'employees':employees})

@login_required
def delete(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/empdata')

@login_required
def update(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/empdata')
	return render(request,'proapp/update.html',{'employee':employee})

def news(request):
	return render(request,'proapp/addnews.html')

def logout(request):
	return render(request,'proapp/logout.html')

def signup(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'proapp/signup.html',{'form':form})