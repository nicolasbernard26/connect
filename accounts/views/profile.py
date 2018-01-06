from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from events.models import Event, Involvement, PhotoEvent

@login_required()
def profile_view(request):
    user = request.user
    profile = user.profile_user
    involves = Involvement.objects.filter(profile=profile) # pylint: disable=no-member
    for involve in involves:
        involve.event.photos = PhotoEvent.objects.filter(event=involve.event) # pylint: disable=no-member
        if len(involve.event.photos) > 6:
            involve.event.photos = involve.event.photos[slice(0, 6, 1)]

    my_events = Event.objects.filter(admin=profile)       # pylint: disable=no-member
    return render(request, 'accounts/profile.html', locals())