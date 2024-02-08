from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.



def FVB(request):
    return HttpResponse('This is tha string from fbc_string')


class CBV_String(View):
    def get(self,request):
        return HttpResponse('This is tha string from CBV_string')





def FVB_html(request):
    return render(request,'FVB_html.html')


class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')



def InsertSchoolForm(request):
    SO=SchoolForm()
    d={'SO':SO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolForm by using FBv is done')
    return render(request,'InsertSchoolForm.html',d)

class InsertShoolForm_by_CBV(View):
    def get(self,request):
        CO=SchoolForm()
        d1={'CO':CO}
        return render(request,'InsertShoolForm_by_CBV.html',d1) 

    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByCbv is done')


    class CBV(TemplateView):
        template_name='Cbv_Template.html'

