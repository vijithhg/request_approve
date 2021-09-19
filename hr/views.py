from django.shortcuts import redirect, render
from .forms import CreateUserForm
from employee.models import LeaveRequest

# Create your views here.

def home(request):
    return render(request,'dashboard_hr.html')

def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'emp_registration.html',context)

def pendingLeaveRequest(request):
    Pending = LeaveRequest.objects.all().filter(status=False)
    context={'Pending':Pending}
    return render(request, 'pendingReq.html',context)

def approveLeave (request,pk):
    LeaveStatus = LeaveRequest.objects.get(id=pk)
    LeaveStatus.status=True
    LeaveStatus.save()
    return redirect('hr_approved_leave.html')

def viewLeave(request):
    ViewLeave= LeaveRequest.objects.all().filter(status=True)
    context ={'ViewLeave':ViewLeave}
    return render(request, 'hr_approved_leave.html',context)