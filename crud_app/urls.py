from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='empList'),
    path('add/',views.addemp,name='addEmployee'),
    path('delete/',views.delemp,name='deleteEmployee'),
    path('update/',views.upemp,name='updateEmployee'),
]