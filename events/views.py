from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from events.models import Event, Involvement, PhotoEvent

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


@login_required()
def detail(request, id_event):
    my_event = Event.objects.get(id=id_event)           # pylint: disable=no-member
    photos = PhotoEvent.objects.filter(event=my_event)  # pylint: disable=no-member
    my_event.photos_left = photos[slice(0, None, 2)]
    my_event.photos_right = photos[slice(1, None, 2)]

    return render(request, 'events/detail.html', locals())

