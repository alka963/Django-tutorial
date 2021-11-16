from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def table(request):
    num1 = dict()
    number = int(request.GET.get('number'))
    for ctr in range(1, 11):
        num1[ctr] = number * ctr
    return render(request, 'myapp/table.html',{'result': num1, 'number': number})