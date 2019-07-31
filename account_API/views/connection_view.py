from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from account.constant.choices.notification_types import NOTIFICATION_TYPES
from account.models.notification_model import NotificationModel
from account.repository.notification_repository import NotificationRepository
from account.repository.profile_repository import ProfileRepository
from account_API.serializers import ProfileSerializer, ConnectionSerializer, ConnectionProfileSerializer, NonConnectionProfileSerializer
from event_API.serializers import InvolvementSerializer
from account.models.profile_model import ProfileModel

from django.contrib.auth.models import User


import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class ConnectionView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = ConnectionSerializer(request.user.profile_user, many=False)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        profile: ProfileModel = get_object_or_404(ProfileModel, user=request.user)
        id_other_profile = request.data.__getitem__("id_other_profile")
        notification_type = NOTIFICATION_TYPES.__getitem__('add')
        notification: NotificationModel = NotificationRepository().create(id_other_profile,
                                                                          profile.id,
                                                                          notification_type)
        notification.save()
        return JsonResponse({"error": "no_error", "notification_id": notification.id}, safe=False)
