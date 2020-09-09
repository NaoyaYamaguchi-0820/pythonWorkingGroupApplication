# 独自追加 pythonWorkingGroupApplication/urls.pyより転送される。

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('form/', views.form, name="form"),
    path('allList/', views.allList, name="allList"),

    path('example_form/', views.example_form, name="example_form"),
    path('example_create/', views.example_create, name="example_create"),

]
