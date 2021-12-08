from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
# Create your views here

def Registration(request):
    if request.method == 'POST':
        emp_frm = UserRegisterForm(request.POST)
        if emp_frm.is_valid():
            emp_frm.save()
    else:
        emp_frm = UserRegisterForm()
    di = {'emp_frm':emp_frm}
    return render(request, 'myapp/register.html', context=di)

def Login(request):
    if request.method == 'POST':
        emp_frm = AuthenticationForm(request=request, data=request.POST)
        if emp_frm.is_valid():
            username = emp_frm.cleaned_data['username']
            password = emp_frm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            global dict
            dict = {'username':username, 'password':password}
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
    else:
        emp_frm = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form':emp_frm})

def home(request):
    return render(request, 'myapp/home.html', dict)