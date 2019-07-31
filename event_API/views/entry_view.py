from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from event.models.event_model import EventModel
from event.models.involvement_model import InvolvementModel
from event_API.serializers import InvolvementSerializer
from account.models.profile_model import ProfileModel
from event_API.serializers import EventSerializer
from account.models.profile_model import ProfileModel
from django.core.files.images import ImageFile

import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class EntryView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, id_event):
        user = get_object_or_404(ProfileModel, user=request.user)
        involve = user.involves.all().filter(event=id_event)

        if involve.count() == 1:
            print(involve[0].event.entries)
            return JsonResponse({"entries": ""}, safe=False)

        else:
            return JsonResponse({"erreur": "You are not authorized"}, safe=False)
