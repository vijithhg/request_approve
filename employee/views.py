from functools import reduce
from django.contrib.auth import authenticate,login
from django.db import models
from django.shortcuts import redirect, render
from .models import LeaveRequest
from .forms import LeaveRequestForm

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard/')
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard_emp.html')

def leaveRequest(request):
    form = LeaveRequestForm()
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_emp')
    context={'form':form}
    return render(request, 'leaveRequest.html',context)

def leaveStatus(request):
    status = LeaveRequest.objects.all()
    context={'status':status}
    return render(request,'view_leavestatus.html',context)