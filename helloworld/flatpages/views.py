#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
 return render(request,'index.html',{})

def home2(request):
 return render(request,'static_handler.html',{})
