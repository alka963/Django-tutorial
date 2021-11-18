from django import forms
class Employee(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField(max_length=20)
    esal = forms.FloatField()
    eaddress = forms.CharField(max_length=20)
    eemail = forms.EmailField()