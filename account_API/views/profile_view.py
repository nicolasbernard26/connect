from django.http import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView

from account.repository.profile_repository import ProfileRepository
from account_API.serializers import ProfileSerializer, ConnectionProfileSerializer, NonConnectionProfileSerializer
from account.models.profile_model import ProfileModel

import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class ProfileView(APIView):

    def get(self, request, id):
        """
        """
        if request.user.profile_user.id == int(id):
            profile_object = request.user.profile_user
            profile_serialized = ProfileSerializer(profile_object, many=False)
            profiles = ProfileModel.objects.all() \
                .exclude(id__in=profile_object.connections.all()) \
                .exclude(id=profile_object.id) \
                .annotate(connections_count=Count('connections')) \
                .order_by('connections_count')
            print(profiles)
            profiles_serialized = ProfileSerializer(profiles, many=True)
            return JsonResponse({"profile": profile_serialized.data,
                                 "relation": "profile",
                                 "profile_to_add": profiles_serialized.data}, safe=False)

        elif request.user.profile_user.connections.filter(id=id).count() == 1:
            profile = ConnectionProfileSerializer(ProfileModel.objects.get(id=id), many=False)
            return JsonResponse({"profile" : profile.data, "relation": "connection"}, safe=False)

        else:
            profile = NonConnectionProfileSerializer(ProfileModel.objects.get(id=id), many=False)
            return JsonResponse({"profile": profile.data, "relation": "non_connection"}, safe=False)

    def post(self, request):
        """
        """
        profile_created: ProfileModel = ProfileRepository().create(request.data, request.FILES)
        ProfileRepository().save(profile_created)
        return JsonResponse({"authenticated": profile_created.id}, safe=False)