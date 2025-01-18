from django.shortcuts import render,redirect
from .models import userdata,image
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        registeruser=userdata.objects.filter(email=email,password=password)
        if registeruser.exists():
            request.session['email']=email
            return redirect('/home/')
        else:
            messages.error(request,"Email or Password doesnot exists")
            return render(request,'signup.html')
    return render(request,'login.html')


def signup(request,method=['GET','POST']):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        conf_password=request.POST.get('conf_password')
        existuser=userdata.objects.filter(email=email)
        if existuser.exists():
            messages.error(request,"email already exists")
        elif password!=conf_password:
            messages.error(request,"Password doesnt match")
        else:
            userdata.objects.create(email=email,password=password)
            return redirect('/login/')
    return render(request,'signup.html')

def home(request):
    de_image=image.objects.all()
    return render(request,'home.html',{'images':de_image}) 


def appoinment(request):
    return render(request,'appoinment.html')

def appname(request,id):
    name=image.objects.get(id=id)
    return render(request,'appoinment.html',{'name':name})

def bill(request):
    return render(request,'bill.html')

def search(request):
    query=request.GET.get("q")
    if query=='':
        return redirect('home')
    else:
        result=image.objects.filter(dr_name__icontains=query)
        return render(request,'home.html',{'result':result})