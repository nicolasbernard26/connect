from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from event.models.photo_event_model import PhotoEventModel
from event_API.serializers import PhotoSerializer
from account.models.profile_model import ProfileModel
from django.core.files.images import ImageFile

import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class ConnectAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def getProfile(request):

