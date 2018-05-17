from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from account_API.serializers import ProfileSerializer

from django.contrib.auth.models import User

import logging

logging.basicConfig(filename='log/account_API.log', level=logging.DEBUG)
logging.info('Initialization of account_API')


class LoginView(APIView):

    permission_classes = ()

    def get(self, request):
        """
        """
        serializer = ProfileSerializer(request.user.profile_user, many=False)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        user = User.objects.get(username=request.data.get("username"))
        if user.check_password(request.data.get("password")) and not user.is_anonymous:
            token = Token.objects.get_or_create(user=user)
            profile = ProfileSerializer(user.profile_user, many=False)
            return JsonResponse({"authenticated": "true", "token": str(token[0]), "profile": profile.data}, safe=False)
        else:
            return JsonResponse({"authenticated": "false"}, safe=False)
