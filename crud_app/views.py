from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Employee

# Create your views here.
def index(request):
    allEmp = Employee.objects.all()
    return render(request, 'index.html',{'allEmp':allEmp})

def addemp(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            emp_exists = Employee.objects.filter(name=name).exists()
            if emp_exists:
                messages.error(request, 'Name already exist!!!')
                return render(request, 'add.html')
            else:
                Employee(name=name, email=email, phone=phone).save()
                messages.success(request, "Employee added successfully.")
                return render(request, 'add.html')
        else:
            return render(request, 'add.html')
    except Exception as e:
        print(e)
        return render(request, 'index.html')

def delemp(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            emp_exists = Employee.objects.filter(name=name).exists()
            if not emp_exists:
                messages.error(request, 'Employee not found!!!')
                return render(request, 'delete.html')
            else:
                Employee.objects.filter(name=name).delete()
                messages.success(request, 'Employee Deleted Successfully.')
                return render(request, 'delete.html')
        else:
            return render(request, 'delete.html')
    except Exception as e:
        print(e)
        allEmp = Employee.objects.all()
        return render(request, 'index.html',{'allEmp':allEmp})

def upemp(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            newName = request.POST['name']
            newEmail = request.POST['email']
            newPhone = request.POST['phone']
            emp = Employee.objects.filter(id=id).first()
            if not emp:
                messages.info(request, 'Employee not found!!!')
                return render(request, 'update.html')
            else:
                if newName:
                    if Employee.objects.filter(name=newName):
                        messages.error(request, 'Name already exists!!!')
                        return render(request, 'update.html') 
                    else:
                        emp.name = newName
                if newEmail:
                    emp.email = newEmail
                if newPhone:
                    emp.phone = newPhone
                emp.save()
                messages.success(request, 'Employee updated successfully.')
                return render(request, 'update.html')
        else:
            return render(request, 'update.html')
    except Exception as e:
        print(e)
        return render(request, 'update.html')
