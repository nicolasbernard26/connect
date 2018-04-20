from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


from rest_framework.authtoken.models import Token

from account_rest.serializers import ProfileSerializer, ConnectionSerializer, ConnectionProfileSerializer, NonConnectionProfileSerializer
from event_rest.serializers import InvolvementSerializer
from account.models.profile_model import Profile

from django.contrib.auth.models import User

from django.core.files.images import ImageFile

import json

# Create your views here.
@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def profile(request, id):
    """
    """
    print(id)
    print(request.user.profile_user.id)
    if request.user.profile_user.id == int(id):    
        profile = ProfileSerializer(request.user.profile_user, many=False)
        return JsonResponse({"profile" : profile.data, "relation" : "profile"}, safe=False)
    elif request.user.profile_user.connections.filter(id=id).count() == 1:
        profile = ConnectionProfileSerializer(Profile.objects.get(id=id), many=False)
        return JsonResponse({"profile" : profile.data, "relation": "connection"}, safe=False)
    else :
        profile = NonConnectionProfileSerializer(Profile.objects.get(id=id), many=False)
        return JsonResponse({"profile" : profile.data, "relation": "non_connection"}, safe=False)


@api_view(['GET', 'POST'])
@permission_classes(())
def login(request):
    """
    """
    if request.method == 'GET':
        serializer = ProfileSerializer(request.user.profile_user, many=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        user = User.objects.get(username=request.data.get("username"))
        if user.check_password(request.data.get("password")) and not user.is_anonymous:
            token = Token.objects.get_or_create(user=user)
            profile = ProfileSerializer(user.profile_user, many=False)
            return JsonResponse({"authenticated": "true", "token": str(token[0]), "profile": profile.data}, safe=False)
        else:
            return JsonResponse({"authenticated": "false"}, safe=False)


"""
DETAIL :
"""
@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def connections(request):
    """
    """
    if request.method == 'GET':
        serializer = ConnectionSerializer(request.user.profile_user, many=False)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def events(request):
    """
    """
    if request.method == 'GET':
        serializer = InvolvementSerializer(request.user.profile_user.involve, many=True)
        print(serializer.data)
        return JsonResponse({ "events" : serializer.data}, safe=False)
