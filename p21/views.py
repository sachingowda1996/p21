from django.http import HttpResponse
from django.shortcuts import render

def html_demo1(request):
    return render(request,"sample.html")
def html_demo2(request):
    return render(request,"sample1.html")    