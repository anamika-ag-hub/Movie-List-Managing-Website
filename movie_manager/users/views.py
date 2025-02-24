from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import login as authlogin,logout as authlogout
from django.contrib.auth import authenticate
def login(request):
  error_message=None

  if request.POST:
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(username=username,password=password)
      if user:
         authlogin (request,user)
         return redirect('list')
      else: 
         error_message='invalid credential'   
  
    
  return render(request,'users/login.html',{'error_message':error_message})
def signup(request):
 user=None
 error_message=None
 
 if request.POST:
    username=request.POST['username']
    password=request.POST['password']
    try:
       user=User.objects.create_user(username=username,password=password)
       return redirect('login')
    except Exception as e:
      error_message=str(e)   

 return render(request, 'users/signup.html', {'user': user, 'error_message': error_message})
def logout(request):
   authlogout(request)
   return redirect('login')