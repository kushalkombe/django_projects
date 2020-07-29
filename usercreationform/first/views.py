from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from first.forms import UserRegistrationForm, ImageModelForm
from django.contrib import messages, auth
from first.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def user_registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"user registered successfully {user}")
            #return redirect('/admin/')
    return render(request,'first/home.html',{'form':form})

def success_view(request):
    return render(request,'first/success.html')

def add_image(request):
    form = ImageModelForm()
    if request.method == "POST":
        form = ImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/first/success/')
    return render(request,'first/add.html',{'form':form})

@login_required
def img_fetch(request):
    imgs = ImageModel.objects.all()
    print(imgs)
    return render(request,'first/success.html',{'imgs':imgs})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username = username, password = password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('/first/fetch/')
            else:
                messages.error(request,'Invalid username or password')
        except ObjectDoesNotExist:
            print('object does not exists')
    return render(request,'first/login2.html')

def logout(request):
    auth.logout(request)
    return render(request,"first/login2.html")
