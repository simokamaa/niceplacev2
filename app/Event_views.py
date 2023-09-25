from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# view for creating new Event
def Event_create(request):
    form = EventForm(request.POST)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/Events_detail/')
    else:
        form = EventForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, 'Dashboard/Event_create.html', context)

# view for reading all Events
def Events_detail(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }
    return render(request, 'Dashboard/Events_detail.html', context)

# view for reading a single user

def Event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event' : event
    }
    return render(request, 'Dashboard/Event_detail.html', context)

# view for updating a single user
def Event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST, instance = event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance = event)
        if form.is_valid():
            form.save()
            return redirect('/home/Events_detail/')
    else:
        form = EventForm(request.POST, instance = event)
    context = {
        'form' : form,
        'event' : event
    }
    return render(request, 'Dashboard/Event_update.html', context)

#view for deleting a single user
def Event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('/home/Events_detail/')

# view for deleting all users
def Events_delete(request):
    events = Event.objects.all()
    events.delete()
    return redirect('/home/Events_detail/')

        
    