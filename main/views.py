from django.views import generic
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def  form(request):
    # TODO 生年月日セレクトボックス表示のためのテストコード　<<ここから>>
    yearList = range(1900, 2021)
    monthList = range(1, 13)
    dayList = range(1, 32)
    return render(request, 'pages/form.html', {
        'yearList': yearList,
        'monthList': monthList,
        'dayList': dayList,
    })
    # テストコード<<ここまで>>

def allList(request):
    return render(request, 'pages/allList.html')