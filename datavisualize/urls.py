from django.urls import path
from .views import *

urlpatterns=[
    path(r'data/',index,name="index-data"),path(r'json/data/',get_data),
    path(r'chart/data/',ChartData.as_view()),path(r'',index,name="index"),
    path(r'ajax/',Ajax),path('record/',Record),path(r'py/',PyImage),
]