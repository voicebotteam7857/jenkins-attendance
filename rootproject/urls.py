"""
URL configuration for rootproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from attendance import views as attendance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',attendance_views.home, name = 'home'),
    path('add/employee/',attendance_views.create_employee , name='create_employee'),
    path('employee/edit/<int:employee_id>/', attendance_views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:employee_id>/', attendance_views.delete_employee, name='delete_employee')
    
]
