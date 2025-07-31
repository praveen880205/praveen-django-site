from django.shortcuts import render,redirect
from django. urls import path
from django import urls
from .models import Datas

def new(request):
    if request.method=='POST':
        names=request.POST.get('name')
        adresss=request.POST.get('adress')
        gmails=request.POST.get('gmail')
        phones=request.POST.get('phone')
        a=Datas(NAME=names,Address=adresss,Gmail=gmails,Phone=phones)
        a.save()
        return redirect('/data/')
    
    return render(request,'web.html')
def summa(request):
    b=Datas.objects.all()
    return render(request,'summa.html',{'b':b})

def contact(request):
    return render(request,'contact.html')
    
