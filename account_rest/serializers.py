from rest_framework import serializers

from django.contrib.auth.models import User

from event.models.involvement import Involvement
from event.models.event import Event
from account.models.profile_model import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class WeakProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = False)
    
    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'background', 'user',)


class EventSerializer(serializers.ModelSerializer):
    admin = WeakProfileSerializer(read_only = True)
    
    class Meta:
        model = Event
        fields = ('title', 'id', 'admin', 'place', 'description', 'date_start', 'date_end', 'theme', 'photo_event')
        
class InvolvementSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only = True)
    
    class Meta:
        model = Involvement
        fields = ('event',)


## ACCOUNT SERIALIZER :
class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = False)
    involves = InvolvementSerializer(read_only = True, many = True)
    connections = WeakProfileSerializer(read_only = True, many = True)
    
    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'background', 'user', 'involves', 'connections')

class ConnectionProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = False)
    involves = InvolvementSerializer(read_only = True, many = True)
    connections = WeakProfileSerializer(read_only = True, many = True)
    
    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'background', 'user', 'involves', 'connections')

class NonConnectionProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = False)
    
    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'background', 'user')

class ConnectionSerializer(serializers.ModelSerializer):
    connections = ProfileSerializer(read_only = True, many = True)

    class Meta:
        model = Profile
        fields = ('connections',)
