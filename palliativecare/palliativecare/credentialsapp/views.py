from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
# def registertemp(request):
#     return  render(request,"registrationtemp.html")
# def logintemp(request):
#     return  render(request,"logintemp.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('logintemp')
    return render(request,"logintemp.html")

def register_home(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confpassword = request.POST['confpassword']
        if password==confpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken.Try with another username.")
                return redirect('registertemp')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken.Try with another email id.")
                return redirect('registertemp')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                user.save();
                return redirect('logintemp')
        else:
            messages.info(request,"Password not matching.Try Again.")
            return redirect('registertemp')
        return redirect('/')

    return render(request,"registrationtemp.html")

def logout(request):
    auth.logout(request)
    return redirect('/')