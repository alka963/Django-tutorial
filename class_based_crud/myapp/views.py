from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import Employeeform
# Create your views here.
class Home(ListView):
    model = Employee
    template_name = 'myapp/home.html'
class AddRecord(CreateView):
    model = Employee
    form_class = Employeeform
    template_name = 'myapp/add.html'
    success_url = '/'

class UpdateRecord(UpdateView):
    model = Employee
    form_class = Employeeform
    pk_url_kwarg = 'pk'
    template_name = 'myapp/update.html'
    success_url = '/'

class DeleteRecord(DeleteView):
    model = Employee
    pk_url_kwarg = 'pk'
    template_name = 'myapp/delete.html'
    success_url = '/'