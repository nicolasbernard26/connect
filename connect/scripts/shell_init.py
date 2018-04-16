from django.contrib.auth.models import User
from accounts.models import Profile, Follow 
from events.models import Involvement, Event

user = User.objects.get(username="justine")
profile = Profile.objects.get(user=user)

all_profiles = Profile.objects.all()

list = []

for other_profile in all_profiles:
	common = profile.following.all().values('following').intersection(other_profile.following.all().values('following'))
	list.append({"name": other_profile.getName(), "common_following": common})