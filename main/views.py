from django.views import generic
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def  form(request):
    return render(request, 'pages/form.html')

def allList(request):
    return render(request, 'pages/allList.html')