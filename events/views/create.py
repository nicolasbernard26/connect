from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event, Involvement, PhotoEvent

from events.forms import EventForm


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

