from django.shortcuts import render
from .models import Employee
# Create your views here.
def search_all(request):
    emp_list = Employee.objects.all()
    d = {'emp_list': emp_list}
    return render(request, 'myapp/index.html', context=d)
