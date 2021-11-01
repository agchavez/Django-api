
from api.users.serializers.users import UserModelSerializer, UserSingupSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers 

from api.users.serializers import UserLoginSerializer
from api.users.models import Client, User


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user , token = serializer.save()
        data= {
            'msj': UserModelSerializer(user).data,
            'token':token
        }
        return Response(data, status = status.HTTP_201_CREATED)
class UserSignupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSingupSerializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status = status.HTTP_201_CREATED)
        