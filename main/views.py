from django.views import generic
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Employee
from .forms import EmployeeModelForm
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'index.html')

def  form(request):
    form = EmployeeModelForm()
    return render(
        request, 
        'pages/form.html', 
        {
        'form': form,
    })

def allList(request):
    employeeList = Employee.objects.all()
    return render(
        request,
        'pages/allList.html',
        {
            'employeeList': employeeList,
        },
    )

# example_form.html 初期表示
def example_form(request):
    form = EmployeeModelForm()
    return render(
        request,
        'pages/example_form.html',
        {
            'form': form,
        },
    )

# 登録処理時
@require_POST
def example_create(request):
    
    employeeInfomation = Employee()
    
    form = EmployeeModelForm(request.POST,instance=employeeInfomation)

    if form.is_valid():
        form.save()
        return redirect('main:allList')
    else:
        return render(
            request,
            'pages/form.html',
            {
                'form': form,
            },
        )
