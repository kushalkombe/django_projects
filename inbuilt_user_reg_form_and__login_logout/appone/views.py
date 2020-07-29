from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def user_registration(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            print(user)
            form.save()
            messages.success(request,f'user registered successfully {user}')
            return redirect('/login/')

    return render(request,'appone/home.html',{'form':form})

def success_view(request):
    return render(request,'appone/success.html')

def add_image(request):
    form=ImageModelForm()
    if request.method=='POST':
        form=ImageModelForm(request.POST, request.files)
        if form.is_valid():
            form.save()
            return redirect('appone/success/')
    return render(request,('appone/add.html',{'form':form}))
