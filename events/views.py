from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event, Involvement, PhotoEvent

from .forms import EventForm


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


@login_required()
def create(request):
    form = EventForm(request.POST or None, request.FILES)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        envoi = True
        event = form.save(commit=False)  # Ne sauvegarde pas directement l'article dans la base de données
        event.admin = request.user.profile_user
        event.save()
    return render(request, 'events/create.html', locals())

