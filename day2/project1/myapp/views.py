from django.shortcuts import render
from datetime import datetime


# Create your views here.
def home(request):
    dt = datetime.now()
    h = dt.hour
    if 12 > h > 5:
        d = {'dt': "Good Morning Alka!!!"}
    elif 16 > h > 12:
        d = {'dt': "Good After Noon Alka!!!"}
    elif 19 > h > 16:
        d = {'dt': "Good Evening Alka!!!"}
    else:
        d = {'dt': "Good Night Alka!!!"}
    return render(request, 'myapp/index.html', context=d)
