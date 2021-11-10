from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    date = '''<h1> Current Date and Time:</h1>''',datetime.now()
    return HttpResponse(date)
