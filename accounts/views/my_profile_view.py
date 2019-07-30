from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event, Involvement, PhotoEvent
from accounts.models import Profile, Follow

from accounts.utils.common_following import Common_following, getCommonFollowing


@login_required()
def my_profile_view(request):
    user = request.user
    profile = user.profile_user
    

    my_photos = profile.own_photo.all()

    following = profile.following.all()
    followers = profile.followers.all()

    nb_following = len(following)
    no_following = nb_following == 0
    nb_followers = len(followers)
    no_followers = nb_followers == 0

    my_events = profile.creator.all()
    events = profile.involve.all()


    all_other_profiles = Profile.objects.all().exclude(id__in=[fol.following.id for fol in following]).exclude(id=profile.id)
    list_common = []

    for other_profile in all_other_profiles:
        common = other_profile.following.all().filter(following__in=[fol.following for fol in following]).count()
        list_common.append(Common_following(other_profile.getName(), common))
    
    list_common = sorted(list_common, key=getCommonFollowing, reverse=True)
    return render(request, 'accounts/my_profile.html', locals())