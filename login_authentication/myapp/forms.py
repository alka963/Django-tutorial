from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
from django import forms
class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


