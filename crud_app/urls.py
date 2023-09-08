from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add/',views.addemp),
    path('delete/',views.delemp),
    path('update/',views.upemp),
]