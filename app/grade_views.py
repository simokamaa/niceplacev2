from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# view for creating new grade
def grade_create(request):
    form = GradeForm(request.POST)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/grades_detail/')
    else:
        form = GradeForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/grade_create.html', context)

# view for reading all grades
def grades_detail(request):
    grades = Grade.objects.all()
    context = {
        'grades' : grades
    }
    return render(request, 'Dashboard/grades_detail.html', context)

# view for reading a single user

def grade_detail(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    context = {
        'grade' : grade
    }
    return render(request, 'Dashboard/grade_detail.html', context)

# view for updating a single user
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    form = GradeForm(request.POST, instance = grade)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance = grade)
        if form.is_valid():
            form.save()
            return redirect('/home/grades_detail/')
    else:
        form = GradeForm(request.POST, instance = grade)
    context = {
        'form' : form,
        'grade' : grade
    }
    return render(request, 'Dashboard/grade_update.html', context)

#view for deleting a single user
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    grade.delete()
    return redirect('/home/grades_detail/')

# view for deleting all users
def grades_delete(request):
    grade =Grade.objects.all()
    grade.delete()
    return redirect('/home/grade_detail/')

        
    