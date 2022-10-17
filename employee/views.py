from django.shortcuts import render, redirect,  HttpResponse 
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/admin_site')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'emp_crud/index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"emp_crud/show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'emp_crud/edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'emp_crud/edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")
def home(request):
    return HttpResponse("this is home page")
