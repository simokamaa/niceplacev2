from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# view for creating new ExamResult
def ExamResult_create(request):
    form = ExamResultForm(request.POST)
    if request.method == 'POST':
        form = ExamResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/ExamResults_detail/')
    else:
        form = ExamResultForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/ExamResult_create.html', context)

# view for reading all ExamResults
def ExamResults_detail(request):
    Examresults = ExamResult.objects.all()
    context = {
        'Examresults' : Examresults
    }
    return render(request, 'Dashboard/ExamResults_detail.html', context)

# view for reading a single user

def ExamResult_detail(request, pk):
    Examresult = get_object_or_404(ExamResult, pk=pk)
    context = {
        'Examresult' : Examresult
    }
    return render(request, 'Dashboard/ExamResult_detail.html', context)

# view for updating a single user
def ExamResult_update(request, pk):
    Examresult = get_object_or_404(ExamResult, pk=pk)
    form = ExamResultForm(request.POST, instance = Examresult)
    if request.method == 'POST':
        form = ExamResultForm(request.POST, instance = Examresult)
        if form.is_valid():
            form.save()
            return redirect('/home/ExamResults_detail/')
    else:
        form = ExamResultForm(request.POST, instance = Examresult)
    context = {
        'form' : form,
        'Examresult' : Examresult
    }
    return render(request, 'Dashboard/ExamResult_update.html', context)

#view for deleting a single user
def ExamResult_delete(request, pk):
    Examresult = get_object_or_404(ExamResult, pk=pk)
    Examresult.delete()
    return redirect('/home/ExamResults_detail/')

# view for deleting all users
def ExamResults_delete(request):
    Examresult =ExamResult.objects.all()
    Examresult.delete()
    return redirect('/home/ExamResult_detail/')

        
    