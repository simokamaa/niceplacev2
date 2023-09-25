from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new class_block
def class_block_create(request):
    form = Class_blockForm(request.POST)
    if request.method == 'POST':
        form = Class_blockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/class_blocks_detail/')
    else:
        form = Class_blockForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/class_block_create.html', context)

# view for reading all class_blocks
def class_blocks_detail(request):
    Class_blocks = class_block.objects.all()
    context = {
        'Class_blocks' : Class_blocks
    }
    return render(request, 'Dashboard/class_blocks_detail.html', context)

# view for reading a single user

def class_block_detail(request, pk):
    Class_block = get_object_or_404(class_block, pk=pk)
    context = {
        'Class_block' : Class_block
    }
    return render(request, 'Dashboard/class_block_detail.html', context)

# view for updating a single user
def class_block_update(request, pk):
    Class_block = get_object_or_404(class_block, pk=pk)
    form = Class_blockForm(request.POST, instance = Class_block)
    if request.method == 'POST':
        form = Class_blockForm(request.POST, instance = Class_block)
        if form.is_valid():
            form.save()
            return redirect('/home/class_blocks_detail/')
    else:
        form = Class_blockForm(request.POST, instance = Class_block)
    context = {
        'form' : form,
        'Class_block' : Class_block
    }
    return render(request, 'Dashboard/class_block_update.html', context)

#view for deleting a single user
def class_block_delete(request, pk):
    Class_block = get_object_or_404(class_block, pk=pk)
    Class_block.delete()
    return redirect('/home/class_blocks_detail/')

# view for deleting all users
def class_blocks_delete(request):
    Class_block =class_block.objects.all()
    Class_block.delete()
    return redirect('/home/staffs_detail/')

        
    