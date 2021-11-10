from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def first(request):
    date = datetime.now()
    eno = 101
    ename = 'Akash'
    eage = 20
    d = {'date': date, 'eno': eno,'ename': ename,'eage': eage}
    return render(request,'myapp/first.html',context=d)
def second(request):
    date = datetime.now()
    sname = 'Satvik'
    scourse = 'Bca'
    sroll = 10
    d = {'date': date, 'sname': sname,'scourse': scourse,'sroll': sroll}
    return render(request,'myapp/second.html',context=d)
def third(request):
    date = datetime.now()
    d = {'date':date}
    return render(request,'myapp/third.html',context=d)