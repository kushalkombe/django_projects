from django.shortcuts import render, redirect
from first.models import Emp
from django.views import View
from first.forms import EmpForm

# Create your views here.
def all_view(request):
    print(request)
    obj = Emp.objects.all()
    return render(request,'first/all.html',{'obj':obj})

class Delete(View):
    def get(self, request, **kwargs):
        print(kwargs)
        id = kwargs.get('id')
        obj = Emp.objects.get(pk = id)
        obj.delete()
        return redirect('/first/all/')

class Update(View):
    def get(self,request, id):
        obj = Emp.objects.get(pk = id)
        return render(request, 'first/update.html',{'obj':obj})

    def post(self, request, **kwargs):
        id = kwargs.get('id')
        obj = Emp.objects.get(pk = id)
        obj.name = request.POST.get('name')
        obj.salary = request.POST.get('salary')
        obj.company = request.POST.get('company')
        obj.save()
        return redirect('/first/all/')

class Add(View):
    def get(self,request):
        form = EmpForm()
        return render(request,'first/add.html',{'form':form})

    def post(self,request):
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/first/all/')
        return render(request, 'first/add.html')
