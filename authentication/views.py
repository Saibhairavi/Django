from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpwd=request.POST.get('cpwd')

        myuser=User.objects.create_user(username=username,email=email,password=password)
        
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'Account created successfully!!')

        return redirect('signin')

    return render(request,'authentication/signup.html')

def signin(request):

    if request.method=='POST':
        username=request.POST['username']
        print(username)        
        password=request.POST['password']      
        user=authenticate(username=username,password=password)
        
        if user is not None: 
            fname=user.first_name      
            login(request,user)   
                      
            return render(request,'authentication/index.html',{'fname':fname})
        else:
            print('not authenticated')
            messages.error(request,'Kindly provide correct credentials to sign-in')
            return redirect('home')


    return render(request,'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('home')

def login_form(request):
    #create form object and pass it for template.
    form=LoginForm(auto_id=True,label_suffix="--")
    return render(request,'authentication/login.html',{'form':form})