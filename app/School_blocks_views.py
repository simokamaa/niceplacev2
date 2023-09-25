from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new School_blocks
def School_blocks_create(request):
    form = School_blocksForm(request.POST)
    if request.method == 'POST':
        form = School_blocksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/School_blockss_detail/')
    else:
        form = School_blocksForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/School_blocks_create.html', context)

# view for reading all School_blockss
def School_blockss_detail(request):
    school_blockss = School_blocks.objects.all()
    context = {
        'school_blockss' : school_blockss
    }
    return render(request, 'Dashboard/School_blockss_detail.html', context)

# view for reading a single user

def School_blocks_detail(request, pk):
    school_blocks = get_object_or_404(School_blocks, pk=pk)
    context = {
        'school_blocks' : school_blocks
    }
    return render(request, 'Dashboard/School_blocks_detail.html', context)

# view for updating a single user
def School_blocks_update(request, pk):
    school_blocks = get_object_or_404(School_blocks, pk=pk)
    form = School_blocksForm(request.POST, instance = school_blocks)
    if request.method == 'POST':
        form = School_blocksForm(request.POST, instance = school_blocks)
        if form.is_valid():
            form.save()
            return redirect('/home/School_blockss_detail/')
    else:
        form = School_blocksForm(request.POST, instance = school_blocks)
    context = {
        'form' : form,
        'school_blocks' : school_blocks
    }
    return render(request, 'Dashboard/School_blocks_update.html', context)

#view for deleting a single user
def School_blocks_delete(request, pk):
    school_blocks = get_object_or_404(School_blocks, pk=pk)
    school_blocks.delete()
    return redirect('/home/School_blockss_detail/')

# view for deleting all users
def School_blockss_delete(request):
    school_blocks =School_blocks.objects.all()
    school_blocks.delete()
    return redirect('/home/staffs_detail/')

        
    