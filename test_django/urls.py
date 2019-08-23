"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from appointments.views import index, appointment_add, appointment_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index.html'),
    path('appointment/', index, name='index.html'),
    path('appointment/add', appointment_add, name='appointment_add'),
    path('appointment/delete/<int:id>/', appointment_delete, name='appointment_delete'),
]
