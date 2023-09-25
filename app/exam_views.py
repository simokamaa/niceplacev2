from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# view for creating new exam
def exam_create(request):
    form = ExamForm(request.POST)
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/exams_detail/')
    else:
        form = ExamForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/exam_create.html', context)

# view for reading all exams
def exams_detail(request):
    exams = Exam.objects.all()
    context = {
        'exams' : exams
    }
    return render(request, 'Dashboard/exams_detail.html', context)

# view for reading a single user

def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    context = {
        'exam' : exam
    }
    return render(request, 'Dashboard/exam_detail.html', context)

# view for updating a single user
def exam_update(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    form = ExamForm(request.POST, instance = exam)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance = exam)
        if form.is_valid():
            form.save()
            return redirect('/home/exams_detail/')
    else:
        form = ExamForm(request.POST, instance = exam)
    context = {
        'form' : form,
        'exam' : exam
    }
    return render(request, 'Dashboard/exam_update.html', context)

#view for deleting a single user
def exam_delete(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    exam.delete()
    return redirect('/home/exams_detail/')

# view for deleting all users
def exams_delete(request):
    exam =Exam.objects.all()
    exam.delete()
    return redirect('/home/exam_detail/')

        
    