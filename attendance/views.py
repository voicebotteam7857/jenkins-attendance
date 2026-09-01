from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Employee , Attendance
from .forms import EmployeeForm

# Create your views here.

def home(request):
    # return render(request, 'home.html')
    # return HttpResponse('hhh')
    all_employees = Employee.objects.all()
    return render(
        request,
        "home.html",        
        {
            "all_employees": all_employees
        }
        
    )

def create_employee(request):
    # return HttpResponse('create employee')
    # return render(request, 'create_emp.html')
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(
        request,
        'add_employee.html',
        {
            "form":form
        }
    )

def edit_employee(request, employee_id):

    employee = get_object_or_404(
        Employee,
        employee_id=employee_id
    )

    if request.method == "POST":
        form = EmployeeForm(
            request.POST,
            instance=employee
        )
        if form.is_valid():
            form.save()
            return  redirect('home')
    else:
        form = EmployeeForm(instance=employee)

   
    return render(
        request,
        'edit_employee.html',
        {
           "form": form
        }

    )
    

   
    # return HttpResponse('edit profile')

def delete_employee(request, employee_id):
    employee = get_object_or_404(
        Employee,
        employee_id=employee_id
    )

    if request.method == 'POST':
        employee.delete()
        return redirect ('home')

    return render(
        request,
        'delete.employee.html',
        {
            "employee": employee
        }
    )
    
