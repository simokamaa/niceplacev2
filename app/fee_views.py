from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# view for creating new fee
def fee_create(request):
    form = FeeForm(request.POST)
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/fees_detail/')
    else:
        form = FeeForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/fee_create.html', context)

# view for reading all fees
def fees_detail(request):
    fees = Fee.objects.all()
    context = {
        'fees' : fees
    }
    return render(request, 'Dashboard/fees_detail.html', context)

# view for reading a single user

def fee_detail(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    context = {
        'fee' : fee
    }
    return render(request, 'Dashboard/fee_detail.html', context)

# view for updating a single user
def fee_update(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    form = FeeForm(request.POST, instance = fee)
    if request.method == 'POST':
        form = FeeForm(request.POST, instance = fee)
        if form.is_valid():
            form.save()
            return redirect('/super_admin/fees_detail/')
    else:
        form = FeeForm(request.POST, instance = fee)
    context = {
        'form' : form,
        'fee' : fee
    }
    return render(request, 'Dashboard/fee_update.html', context)

#view for deleting a single user
def fee_delete(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    fee.delete()
    return redirect('/super_admin/fees_detail/')

# view for deleting all users
def fees_delete(request):
    fee =Fee.objects.all()
    fee.delete()
    return redirect('/super_admin/fee_detail/')

        
    