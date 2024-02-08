from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_views(request):
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request,user)
      return render('website/index.html')

  return render(request,'accounts/login.html')
   
def logout_views(request):
 #   return
    pass
def signup_views(request):
  #  return render(request,'accounts/signup.html')
    pass