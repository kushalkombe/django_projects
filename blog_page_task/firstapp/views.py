from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

def user_registration(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'user registered successfully {user}')
            return redirect('/login/')
    return render(request,'firstapp/home.html',{'form':form})

#
# def success_view(request):
#     obj=Post.objects.all()
#     print(request.user)
#     return render(request,'firstapp/all.html',{'obj':obj})
@login_required
def success_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = PostForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.avatar = generate_avatar(profile)
            profile.save()
            return redirect('/all.html/')
    else:
        form = PostForm(instance=profile)
    return render(request, 'firstapp/all.html', {'form': form})


class Add(View):
    def get(self,request):
        form=PostForm()
        return render(request,'firstapp/add.html',{'form':form})

    def post(self,request):
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
        return render(request,'firstapp/add.html')

class Delete(View):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        obj=Post.objects.get(pk=id)
        obj.delete()
        return redirect('/success/')

class Update(View):
    def get(self,request,id):
        obj=Post.objects.get(pk=id)
        form=PostForm(instance=obj)
        return render(request,'firstapp/update.html',{'form':form,'obj':obj})

    def post(self,request,**kwargs):
        id=kwargs.get('id')
        obj=Post.objects.get(pk=id)
        form=PostForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('/success/')
