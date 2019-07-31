from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from account.repository.profile_repository import ProfileRepository
from account_API.serializers import ProfileSerializer, ConnectionSerializer, ConnectionProfileSerializer, NonConnectionProfileSerializer
from event_API.serializers import InvolvementSerializer
from account.models.profile_model import ProfileModel

from django.contrib.auth.models import User


import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class InvolveView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = InvolvementSerializer(request.user.profile_user.involve, many=True)
        print(serializer.data)
        return JsonResponse({"events": serializer.data}, safe=False)