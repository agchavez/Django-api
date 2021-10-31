"""Class user serializer"""
#Djago 
from django.contrib.auth import authenticate

# Django rest_framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username = data['email'], password = data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return data
    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.contex['user'])
        return self.context, token.key
