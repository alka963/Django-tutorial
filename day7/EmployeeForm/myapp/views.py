from django.shortcuts import render
from .forms import EmployeeForm, Emp
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def add(request):
    emp_frm = EmployeeForm()
    di = {'emp_frm': emp_frm}
    if request.method == 'POST':
        emp_frm = EmployeeForm(request.POST)
        if emp_frm.is_valid():
            emp_frm.save(commit=True)
    return render(request, 'myapp/add.html', context=di)

def update(request):
    emp_frm = EmployeeForm()
    di = {'emp_frm':emp_frm}
    return render(request, 'myapp/update.html', context=di)

def delete(request):
    emp_frm = Emp()
    di = {'emp_frm': emp_frm}
    return render(request, 'myapp/delete.html', context=di)

def Findall(request):
    emp_list = Employee.objects.all()
    di = {'emp_list': emp_list}
    return render(request, 'myapp/findall.html', context=di)
