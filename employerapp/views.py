from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def employerapp(request):
    return render(request,'employerapp/employerhomepage.html')
def crudfunction(request):
    employees=Employerdetails.objects.all()
    return render(request,'employerapp/crud.html',{'employees': employees})

def crud_insert(request):
    if request.method == "POST":
        empid = request.POST['empid']
        empname = request.POST['empname']
        emplocation = request.POST['emplocation']
        empphone = request.POST['empphone']
        empemail = request.POST['empemail']

        add = Employerdetails(
            empid=empid,
            empname=empname,
            emplocation=emplocation,
            empphone=empphone,
            empemail=empemail
        )
        add.save()

        return redirect('crudfunction')  # use url name

    return redirect('crudfunction')

def read_employee(request):
    employees = Employerdetails.objects.all()
    selected_emp = None
    if request.method == "POST":
        read_empid = request.POST.get('read_empid')
        selected_emp = Employerdetails.objects.filter(empid=read_empid).first()
    context = {
        'employees': employees,
        'selected_emp': selected_emp
    }
    return render(request, 'employerapp/crud.html', context)
def update_employee(request):
    employees = Employerdetails.objects.all()
    update_emp = None
    update_msg = None

    if request.method == "POST":
        empid = request.POST.get("empid")
        update_emp = Employerdetails.objects.filter(empid=empid).first()

        # When Update button clicked
        if "update" in request.POST and update_emp:
            update_emp.empname = request.POST.get("empname")
            update_emp.emplocation = request.POST.get("emplocation")
            update_emp.empphone = request.POST.get("empphone")
            update_emp.empemail = request.POST.get("empemail")
            update_emp.save()
            update_msg = "Employee updated successfully"

    return render(request, "employerapp/crud.html", {
        "employees": employees,
        "update_emp": update_emp,
        "update_msg": update_msg
    })
def delete_employee(request):
    employees = Employerdetails.objects.all()
    message = None

    if request.method == "POST":
        empid = request.POST.get("empid")
        emp = Employerdetails.objects.filter(empid=empid).first()

        if emp:
            emp.delete()
            message = f"Employee {empid} deleted successfully"
        else:
            message = "Employee not found"

    return render(request, "employerapp/crud.html", {
        "employees": employees,
        "delete_msg": message
    })