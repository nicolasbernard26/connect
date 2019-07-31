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


class EventView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, id_event=None):
        if id_event is None:
            return JsonResponse({"errors": "URL error"})

        profile: ProfileModel = get_object_or_404(ProfileModel, user=request.user)
        involvement = profile.involves.all().filter(event=id_event)

        if involvement.count() == 1:
            serializer = EventSerializer(involvement[0].event, many=False)
            return JsonResponse({"event": serializer.data}, safe=False)
        else:
            return JsonResponse({"errors": "You are not authorized"}, safe=False)

    def post(self, request):
        profile = get_object_or_404(ProfileModel, user=request.user)
        for file_key in sorted(request.FILES):
            print(file_key)

        event = EventModel(
            title=request.data.get("title"),
            admin=profile,
            place=request.data.get("place"),
            description=request.data.get("description"),
            date_start=request.data.get("date_end"),
            date_end=request.data.get("date_end"),
            photo_event=ImageFile(request.FILES[file_key])
        )
        event.save()
        InvolvementModel(event=event, profile=profile).save()

        return JsonResponse({"id": event.id}, safe=False)

    def update(self, request, id_event):
        profile = get_object_or_404(ProfileModel, user=request.user)
        is_creator = profile.creator.all().filter(id=id_event)
        if is_creator.count() == 1:
            event_to_update = is_creator[0]
            for file_key in sorted(request.FILES):
                event_to_update.photo_event = ImageFile(request.FILES[file_key])
                print(file_key)
            event_to_update.title = request.data.get("title")
            event_to_update.place = request.data.get("place")
            event_to_update.description = request.data.get("description")
            event_to_update.date_start = request.data.get("date_start")
            event_to_update.date_end = request.data.get("date_end")

            event_to_update.save()
            return JsonResponse({"id": event_to_update.id}, safe=False)
        else:
            return JsonResponse({"errors": "You are not authorized"}, safe=False)