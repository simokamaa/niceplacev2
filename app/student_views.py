from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new student
def student_create(request):
    form = StudentForm(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/students_detail/')
    else:
        form = StudentForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/student_create.html', context)

# view for reading all students
def students_detail(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render(request, 'Dashboard/students_detail.html', context)

# view for reading a single user

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student' : student
    }
    return render(request, 'Dashboard/student_detail.html', context)

# view for updating a single user
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST, instance = student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('/home/students_detail/')
    else:
        form = StudentForm(request.POST, instance = student)
    context = {
        'form' : form,
        'student' : student
    }
    return render(request, 'Dashboard/student_update.html', context)

#view for deleting a single user
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('/home/students_detail/')

# view for deleting all users
def students_delete(request):
    staffs =Student.objects.all()
    staffs.delete()
    return redirect('/home/staffs_detail/')

        
    