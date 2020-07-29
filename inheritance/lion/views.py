from django.shortcuts import render

# Create your views here.
def a(request):
    return render (request,'templion/abc.html')

def b(request):
    return render (request,'templion/pqr.html')

def c(request):
    return render (request,'templion/xyz.html')
