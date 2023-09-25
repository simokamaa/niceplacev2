from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


def login(request):
    return render(request, "login.html")

#timetable, messages, elearning, transportations*,library, fee, assignment, notice, plan