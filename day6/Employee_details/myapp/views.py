from django.shortcuts import render
from .forms import Employee
# Create your views here.
def home(request):
    Emp_frm = Employee()
    di = {'Emp_frm': Emp_frm}
    if request.method == 'POST':
        emp_form = Employee(request.POST)
        if emp_form.is_valid():
            eno = emp_form.cleaned_data['eno']
            ename = emp_form.cleaned_data['ename']
            esal = emp_form.cleaned_data['esal']
            eemail = emp_form.cleaned_data['eemail']
            eaddress = emp_form.cleaned_data['eaddress']
            di = {'eno':eno, 'ename': ename, 'esal': esal, 'eemail': eemail, 'eaddress': eaddress}
        return render(request, 'myapp/home.html', context=di)

    return render(request, 'myapp/index.html',context=di)