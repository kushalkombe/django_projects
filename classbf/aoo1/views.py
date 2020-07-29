from django.shortcuts import render,redirect
from aoo1.models import Student
from aoo1.forms import StudentForm
from django.views import View

# Create your views here.
class Fetch(View):
    def get(self,request):
        obj=Student.objects.all()
        return render(request,'aoo1/all.html',{'obj':obj})

class Add(View):
    def get(self,request):
        form=StudentForm()
        return render(request,'aoo1/add.html',{'form':form})

    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/one/fetch/')
        return render(request,'aoo1/add.html')

class Delete(View):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        obj=Student.objects.get(pk=id)
        obj.delete()
        return redirect('/one/fetch/')

class Update(View):
    def get(self,request,id):
        obj=Student.objects.get(pk=id)
        form=StudentForm(instance=obj)
        return render(request,'aoo1/update.html',{'form':form,'obj':obj})

    def post(self,request,**kwargs):
        id=kwargs.get('id')
        obj=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('/one/fetch/')
