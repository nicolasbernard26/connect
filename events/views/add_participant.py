from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pprint import pprint

from events.models import Event, Involvement, PhotoEvent

from accounts.models import Profile

from events.forms import InvolvementForm, MyCustomForm


@login_required()
def add_participant(request, id_event):

    user = request.user
    profile = user.profile_user

    event = Event.objects.get(id=id_event)

    profiles_add = profile.following.all()
    participants = event.participants.all()

    list_profiles = profiles_add.exclude(id__in=[participant.profile.id for participant in participants])

    tuple_res = []
    for l in list_profiles:
        tuple_res.append((l.following.id, l.following.getName()))

    form = MyCustomForm(request.POST, my_choices=tuple_res)

    print(form.is_valid())
    if form.is_valid():
        test = form.cleaned_data["other_field"]
        print("test")
        print(test)
        p = Profile.objects.get(id=test)
        involvement = Involvement(event=event, profile=p)
        involvement.save()

    return render(request, 'events/add_participant.html', locals())