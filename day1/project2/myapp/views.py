from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome</h1>')

def index(request):
    return HttpResponse('<h1>hello everyone</h1>')