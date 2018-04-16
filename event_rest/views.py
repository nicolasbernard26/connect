from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from event.models.involvement import Involvement
from event.models.photoEvent import PhotoEvent
from event.models.event import Event
from event_rest.serializers import EventSerializer, PhotoSerializer
from account.models.profile_model import Profile
from django.core.files.images import ImageFile

# Create your views here.


@api_view(['GET', 'UPDATE'])
@permission_classes((IsAuthenticated, ))
def event(request, id_event):
    """
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'GET':
        involvement = profile.involves.all().filter(event=id_event)

        if involvement.count() == 1:
            serializer = EventSerializer(involvement[0].event, many=False)
            return JsonResponse({"event": serializer.data}, safe=False)
        else:
            return JsonResponse({"error": "You are not authorized"}, safe=False)

    elif request.method == 'UPDATE':
        is_creator = profile.creator.all().filter(id=id_event)
        if is_creator.count() == 1:
            event_to_update = is_creator[0]
            if request.data.get("updatePhoto"):
                for file_key in sorted(request.FILES):
                    event_to_update.photo_event=ImageFile(request.FILES[file_key])
                    print(file_key)
            event_to_update.title = request.data.get("title")
            event_to_update.place = request.data.get("place")
            event_to_update.description = request.data.get("description")

            event_to_update.save()
            return JsonResponse({"id": event_to_update.id}, safe=False)
        else:
            return JsonResponse({"error": "You are not authorized"}, safe=False)



@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def create(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        for file_key in sorted(request.FILES):
            print(file_key)

        event = Event(
            title=request.data.get("title"),
            admin=profile,
            place=request.data.get("place"),
            description=request.data.get("description"),
            date_start=request.data.get("date_end"),
            date_end=request.data.get("date_end"),
            photo_event=ImageFile(request.FILES[file_key])
        )
        event.save()
        Involvement(event=event, profile=profile).save()

        return JsonResponse({"id": event.id}, safe=False)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def photos(request, id_event):
    """
    """
    profile = get_object_or_404(Profile, user=request.user)
    involvement = profile.involves.all().filter(event=id_event)

    if involvement.count() == 1:
        event = involvement[0].event
        if request.method == 'GET':
            serializer = PhotoSerializer(event.photos.all(), many=True)
            return JsonResponse({"photos": serializer.data}, safe=False)

        elif request.method == 'POST':
            for file_key in sorted(request.FILES):
                print(file_key)
                photo = PhotoEvent(
                    photo=ImageFile(request.FILES[file_key]),
                    event=event,
                    owner=profile,
                    title=file_key
                )
                photo.save()
            return JsonResponse({"information": "no_error"})
    else:
        return JsonResponse({"error": "You are not authorized"}, safe=False)


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def set_event_photo(request, id_event):
    user = get_object_or_404(Profile, user=request.user)
    event_query_set = user.creator.all().filter(id=id_event)

    if event_query_set.count() == 1:
        event_to_update = event_query_set[0]
        for file_key in sorted(request.FILES):
            print(file_key)
            event_to_update.photo_event = ImageFile(request.FILES[file_key])
        print(event_to_update.photo_event)
        event_to_update.save()
        return JsonResponse({"update": "pas d'erreur"}, safe=False)

    else:
        return JsonResponse({"error": "You are not authorized"}, safe=False)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def entries(request, id_event):
    """
    """
    user = get_object_or_404(Profile, user=request.user)
    involve = user.involves.all().filter(event=id_event)

    if involve.count() == 1:
        print(involve[0].event.entries)
        return JsonResponse({"entries": ""}, safe=False)

    else:
        return JsonResponse({"erreur": "You are not authorized"}, safe=False)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def delete_photo(request, id_photo):
    """
    """
    profile = get_object_or_404(Profile, user=request.user)
    photo = profile.own_photo.all().filter(id=id_photo)

    if photo.count() == 1:
        photo.delete()
        return JsonResponse({"result": "ok"}, safe=False)

    else:
        return JsonResponse({"erreur": "You are not authorized"}, safe=False)
