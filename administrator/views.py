from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from administrator.forms import BusForm,DriverForm,UserForm
from administrator.models import Bus,Driver
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def index_admin(request):
    drivers=Driver.objects.all()
    current_user=request.user
    if request.method=="POST":
        form=DriverForm(request.POST,request.FILES)
        if form.is_valid():
            driver=form.save(commit=False)
            driver.user=request.user
            driver.save()
            messages.success(request, 'Driver added successfully!')
            return redirect('drivers')
    else:
        form=DriverForm()
        #pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(form, 4)
    return render(request,'main/drivers.html',{'form':form,'drivers':drivers})

def dash_admin(request):
    buses=Bus.objects.all()
    drivers=Driver.objects.all()
    login_details=User.objects.all()
    return render(request,'main/admindash.html',{'buses':buses,'drivers':drivers,'login_details':login_details})

def buses(request):
    buses=Bus.objects.all()
    current_user=request.user
    if request.method=="POST":
        form=BusForm(request.POST,request.FILES)
        if form.is_valid():
            bus=form.save(commit=False)
            bus.user=request.user
            bus.save()
            messages.success(request, 'Bus added successfully!')
            return redirect('buses')
    else:
        form=BusForm()
        #pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(form, 4)
    return render(request,'main/buses.html',{'buses':buses,'form':form})

def navbar(request):
    buses=Bus.objects.all()
    return render(request,'navbar.html',{'buses':buses})

def editbus(request,id):
    bus=Bus.objects.filter(id=id).first()
    if request.method=="POST":
        form=BusForm(request.POST,request.FILES,instance=bus)
        if form.is_valid():
            bus=form.save(commit=False)
            bus.user=request.user
            bus.save()
            messages.success(request, 'Bus updated successfully!')
            return redirect('buses')
    else:
        form=BusForm(instance=bus)
    return render(request,'main/editbus.html',{'bus':bus,'form':form})

def edituser(request,id):
    user=User.objects.filter(id=id).first()
    if request.method=="POST":
        form=UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            user=form.save(commit=False)
            user.user=request.user
            user.save()
            messages.success(request, 'User updated successfully!')
            return redirect('users')
    else:
        form=UserForm(instance=user)
    return render(request,'main/edituser.html',{'user':user,'form':form})

def editdriver(request,id):
    driver=Driver.objects.filter(id=id).first()
    if request.method=="POST":
        form=DriverForm(request.POST,request.FILES,instance=driver)
        if form.is_valid():
            driver=form.save(commit=False)
            driver.user=request.user
            driver.save()
            messages.success(request, 'User updated successfully!')
            return redirect('drivers')
    else:
        form=DriverForm(instance=driver)
    return render(request,'main/editdriver.html',{'driver':driver,'form':form})


def deleteuser(request,id):
    user=User.objects.filter(id=id).delete()
    return redirect('users')

def deletedriver(request,id):
    driver=Driver.objects.filter(id=id).delete()
    return redirect('drivers')

def deletebus(request,id):
    bus=Bus.objects.filter(id=id).delete()
    return redirect('buses')

def users(request):
    users=User.objects.all()
    return render(request,'main/users.html',{'users':users})
