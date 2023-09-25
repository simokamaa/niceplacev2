from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new teacher
def teacher_create(request):
    form = TeacherForm(request.POST)
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/teachers_detail/')
    else:
        form = TeacherForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/teacher_create.html', context)

# view for reading all teachers
def teachers_detail(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers' : teachers
    }
    return render(request, 'Dashboard/teachers_detail.html', context)

# view for reading a single user

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    context = {
        'teacher' : teacher
    }
    return render(request, 'Dashboard/teacher_detail.html', context)

# view for updating a single user
def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST, instance = teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
            return redirect('/home/teachers_detail/')
    else:
        form = TeacherForm(request.POST, instance = teacher)
    context = {
        'form' : form,
        'teacher' : teacher
    }
    return render(request, 'Dashboard/teacher_update.html', context)

#view for deleting a single user
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('/home/teachers_detail/')

# view for deleting all users
def teachers_delete(request):
    teachers = Teacher.objects.all()
    teachers.delete()
    return redirect('/home/teachers_detail/')

        
    