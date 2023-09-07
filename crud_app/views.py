from django.shortcuts import render
from django.contrib import messages
from .models import Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addemployee(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            allEmp = Employee.objects.all()
            for emp in allEmp:
                if name in emp.name:
                    messages.info(request, "Name already exist!!!")
                    return render(request, 'add.html')
            empObj = Employee(name=name, email=email, phone=phone)
            empObj.save()
            messages.success(request, "Employee added successfully.")
            return render(request, 'add.html')
        else:
            return render(request, 'add.html')
    except Exception as e:
        print(e)
        return render(request, 'index.html')