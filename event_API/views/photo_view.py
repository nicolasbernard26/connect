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


class PhotoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id_event):
        profile = get_object_or_404(ProfileModel, user=request.user)
        involvement = profile.involves.all().filter(event=id_event)

        if involvement.count() == 1:
            event = involvement[0].event
            serializer = PhotoSerializer(event.photos.all(), many=True)
            return JsonResponse({"photos": serializer.data}, safe=False)
        else:
            return JsonResponse({"errors": "You are not authorized"}, safe=False)

    def post(self, request, id_event):
        profile = get_object_or_404(ProfileModel, user=request.user)
        involvement = profile.involves.all().filter(event=id_event)

        if involvement.count() == 1:
            event = involvement[0].event
            for file_key in sorted(request.FILES):
                print(file_key)
                photo = PhotoEventModel(
                    photo=ImageFile(request.FILES[file_key]),
                    event=event,
                    owner=profile,
                    title=file_key
                )
                photo.save()
            return JsonResponse({"information": "no_error"})
        else:
            return JsonResponse({"errors": "You are not authorized"}, safe=False)

    def delete(self, request, id_event):
        id_photo = request.GET.get('id_photo', None)

        if id_photo is not None:

            profile = get_object_or_404(ProfileModel, user=request.user)
            photo : PhotoEventModel = profile.own_photos.all().filter(id=id_photo)

            if photo.count() == 1:
                photo.delete()
                return JsonResponse({"result": "ok"}, safe=False)

            else:
                return JsonResponse({"error": "You are not authorized"}, safe=False)
        else:
            return JsonResponse({"error": "Wrong URL parameter"}, safe=False)
