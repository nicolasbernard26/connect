from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event, Involvement, PhotoEvent

from events.forms import EventForm


@login_required()
def detail(request, id_event):
    my_event = Event.objects.get(id=id_event)           # pylint: disable=no-member
    photos = my_event.photos.all()  # pylint: disable=no-member

    
    participants = my_event.participants.all()
    

    nb_participants = len(participants)
    no_participant = nb_participants == 0

    return render(request, 'events/detail.html', locals())

