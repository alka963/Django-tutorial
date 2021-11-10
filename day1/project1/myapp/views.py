from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    page = '''<h1>welcome to my project'''
    return HttpResponse(page)