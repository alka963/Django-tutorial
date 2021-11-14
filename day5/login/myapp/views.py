from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST["username"]
        userpassword = request.POST["userpassword"]
        global di
        di = {'username': username, 'userpassword': userpassword}
        if username == 'alka' and userpassword == 'pass':
            return redirect("/welcome")
        else:
            return redirect("/error")
    return render(request, 'myapp/home.html')

def welcome(request):
    return render(request, 'myapp/welcome.html',di)

def error(request):
    return render(request, 'myapp/error.html', di)