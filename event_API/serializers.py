from rest_framework import serializers
from django.contrib.auth.models import User
from account.models.profile_model import ProfileModel
from event.models.involvement_model import InvolvementModel
from event.models.event_model import EventModel
from event.models.photo_event_model import PhotoEventModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class WeakProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = False)
    
    class Meta:
        model = ProfileModel
        fields = ('id', 'avatar', 'background', 'user',)


class PhotoSerializer(serializers.ModelSerializer):
    owner = WeakProfileSerializer(read_only = True)

    class Meta:
        model = PhotoEventModel
        fields = ('id', 'photo', 'owner', 'title')


class EventSerializer(serializers.ModelSerializer):
    admin = WeakProfileSerializer(read_only = True)
    entries = WeakProfileSerializer(read_only = True, many = True)
    
    class Meta:
        model = EventModel
        fields = ('title', 'id', 'admin', 'place', 'description', 'date_start', 'date_end', 'theme', 'entries', 'photo_event')


class InvolvementSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only = True)
    
    class Meta:
        model = InvolvementModel
        fields = ('event',)
