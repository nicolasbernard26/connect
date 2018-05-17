from rest_framework import serializers

from django.contrib.auth.models import User

from event.models.involvement_model import InvolvementModel
from event.models.event_model import EventModel
from account.models.profile_model import ProfileModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class WeakProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = False)
    
    class Meta:
        model = ProfileModel
        fields = ('id', 'avatar', 'background', 'user',)


class EventSerializer(serializers.ModelSerializer):
    admin = WeakProfileSerializer(read_only = True)
    
    class Meta:
        model = EventModel
        fields = ('title', 'id', 'admin', 'place', 'description', 'date_start', 'date_end', 'theme', 'photo_event')
        
class InvolvementSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only = True)
    
    class Meta:
        model = InvolvementModel
        fields = ('event',)


## ACCOUNT SERIALIZER :
class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = False)
    involves = InvolvementSerializer(read_only = True, many = True)
    connections = WeakProfileSerializer(read_only = True, many = True)
    
    class Meta:
        model = ProfileModel
        fields = ('id', 'avatar', 'background', 'user', 'involves', 'connections')

class ConnectionProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = False)
    involves = InvolvementSerializer(read_only = True, many = True)
    connections = WeakProfileSerializer(read_only = True, many = True)
    
    class Meta:
        model = ProfileModel
        fields = ('id', 'avatar', 'background', 'user', 'involves', 'connections')

class NonConnectionProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = False)
    
    class Meta:
        model = ProfileModel
        fields = ('id', 'avatar', 'background', 'user')

class ConnectionSerializer(serializers.ModelSerializer):
    connections = ProfileSerializer(read_only = True, many = True)

    class Meta:
        model = ProfileModel
        fields = ('connections',)
