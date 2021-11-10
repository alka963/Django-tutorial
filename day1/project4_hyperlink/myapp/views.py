from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def home(request):
    data = '''
    <a href = '/f1'>First Page</a><br>
    <a href = '/f2'>Second Page</a><br>
    <a href = '/f3'>Third Page</a><br>
    '''
    return HttpResponse(data)
def first(request):
    data = '''<a href = '/first'>Back</a><h1>Welcome to my Django Project</h1>'''
    return HttpResponse(data)

def second(request):
    data = '''<a href = '/first'>Back</a><h1>Current Date Time: </h1><hr>''',datetime.now()
    return HttpResponse(data)

def third(request):
    data = '''<a href = '/first'>Back</a><h1> Thank You</h1>'''
    return HttpResponse(data)