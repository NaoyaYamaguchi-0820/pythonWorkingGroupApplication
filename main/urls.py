# 独自追加 pythonWorkingGroupApplication/urls.pyより転送される。

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]
