"""
URL configuration for sampledjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from curd.views import createView, store, index, viewEmp, deleteEmp, updateView, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create',createView),
    path('store',store,name='store'),
    path('',index),
    path('view/<int:pk>',viewEmp,name='viewEmp'),
    path('delete/<int:pk>',deleteEmp,name='deleteEmp'),
    path('update/<int:pk>',updateView, name='updateEmp'),
    path('edit/<int:pk>',update, name='edit'),
]
