"""
URL configuration for project37 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('FVB/',FVB,name='FVB'),
    path('CBV_String/',CBV_String.as_view(),name='CBV_String'),


    path('FVB_html/',FVB_html,name='FVB_html'),
    path('CBV_html/',CBV_html.as_view(),name='CBV_html'),



    path('InsertSchoolForm/',InsertSchoolForm,name='InsertSchoolForm'),
    path('InsertShoolForm_by_CBV/',InsertShoolForm_by_CBV.as_view(),name='InsertShoolForm_by_CBV'),

    path('CBV/',CBV.as_view(),name='CBV'),
    

]
