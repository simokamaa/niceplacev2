from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

def index(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_staffs = Staff.objects.count()
    total_notices = Notice.objects.count()
    context = {
        'total_students' : total_students,
        'total_teachers' : total_teachers,
        'total_staffs' : total_staffs,
        'total_notices' : total_notices,
    }
    return render(request, 'Dashboard/index.html', context)

