from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Place
from . models import Team

def display(request):
    tabledata=Place.objects.all()
    teamdata=Team.objects.all()
    return render(request,'index.html',{'tbdata':tabledata,'teamdetails':teamdata})


# def home(request):
#     return render(request,'formdesign.html')
# def operations(request):
#     a=int(request.GET['num1'])
#     b=int(request.GET['num2'])
#     sum=a+b
#     diff=a-b
#     pro=a*b
#     quo=a/b
#     rem=a%b
#     return render(request,"resultpage.html",{'sum':sum,'difference':diff,'product':pro,'quotient':quo,'remainder':rem})