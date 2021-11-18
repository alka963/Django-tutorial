from django.shortcuts import render
from.models import  Employee
from .forms import EmployeeForm
# Create your views here.
def home(request):
    emp_form = EmployeeForm()
    di = {'emp_form':emp_form}
    if request.method == 'POST':
        empl_form = EmployeeForm(request.POST)
        if empl_form.is_valid():
            empl_form.save(commit=True)
    return render(request, 'myapp/home.html', context=di)

def show(request):
    emp_list = Employee.objects.all()
    di = {'emp_list': emp_list}
    return render(request, 'myapp/show.html', context=di)