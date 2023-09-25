from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new staff
def staff_create(request):
    form = StaffForm(request.POST)
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/staffs_detail/')
    else:
        form = StaffForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/staff_create.html', context)

# view for reading all staffs
def staffs_detail(request):
    staffs = Staff.objects.all()
    context = {
        'staffs' : staffs
    }
    return render(request, 'Dashboard/staffs_detail.html', context)

# view for reading a single user

def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    context = {
        'staff' : staff
    }
    return render(request, 'Dashboard/staff_detail.html', context)

# view for updating a single user
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    form = StaffForm(request.POST, instance = staff)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance = staff)
        if form.is_valid():
            form.save()
            return redirect('/home/staffs_detail/')
    else:
        form = StaffForm(request.POST, instance = staff)
    context = {
        'form' : form,
        'staff' : staff
    }
    return render(request, 'Dashboard/staff_update.html', context)

#view for deleting a single user
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    return redirect('/home/staffs_detail/')

# view for deleting all users
def staffs_delete(request):
    staffs = Staff.objects.all()
    staffs.delete()
    return redirect('/home/staffs_detail/')

        
    