from django.shortcuts import render
from appone.models import Student
from appone.forms import StudentForm
from django.views import View
# Create your views here.
def all_view(request):
    data=Student.objects.all()
    return render(request,'appone/base.html',{'data':data})

def add_view(request):
    form=StudentForm(request.POST)
    if request.method==POST:
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            address=form.cleaned_data.get('address')
            obj=Student.objects.create(name=name,email=email,marks=marks,address=address)
    return render(request,'appone/add.html',{'form':form})
