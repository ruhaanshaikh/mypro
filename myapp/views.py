import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('this is students list')

def date1(request):
    d=datetime.datetime.now()
    return HttpResponse(d)

def index(request):

    a=[
        {'name':'irsahd','age':18,'email':'i@gmail.com'},
        {'name':'faran','age':12,'email':'f@gmail.com'},
        {'name':'samir','age':20,'email':'s@gmail.com'},
        {'name':'lukman','age':17,'email':'l@gmail.com'},
        {'name':'azim','age':22,'email':'a@gmail.com'},

    ]
    return render(request,'index.html',{'a1':a})


def vegitable(request):
    b=[
        {'Veg_Name':'TOMATO','Quantity':12},
        {'Veg_Name':'PATATO','Quantity':0},
        {'Veg_Name':'ONION','Quantity':0},
        {'Veg_Name':'GARLIC','Quantity':90},
        {'Veg_Name':'papers','Quantity':0},
        {'Veg_Name':'cocumber','Quantity':17},

    ]
    return render(request,'vegitable.html',{'b1':b})