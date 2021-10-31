
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.users.serializers import UserLoginSerializer


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user , token = serializer.save()
        data= {
            'msj':'ok',
            'token':'token'
        }
        return Response(data, status = status.HTTP_201_CREATED)
