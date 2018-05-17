from django.http import JsonResponse
from rest_framework.views import APIView

from account.repository.profile_repository import ProfileRepository
from account.models.profile_model import ProfileModel

import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class SignUpView(APIView):

    def post(self, request):
        """
        """
        profile_created: ProfileModel = ProfileRepository().create(request.data, request.FILES)
        ProfileRepository().save(profile_created)
        return JsonResponse({"authenticated": profile_created.id}, safe=False)