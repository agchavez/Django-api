"""Class user serializer"""
#Djago 
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator
from api.users.models.client import Client

# Django rest_framework
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework.authtoken.models import Token


from api.users.models import User, users

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    # profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


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
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class UserSingupSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length = 8, max_length = 64)
    first_name = serializers.CharField(min_length = 3, max_length = 30)
    last_name = serializers.CharField(min_length = 3, max_length = 30)
    username = serializers.CharField(
        min_length = 4,
        max_length = 15,
         validators=[UniqueValidator(queryset=User.objects.all())]
    )

    phone_regex = RegexValidator(
        regex=r'\+?504?\d{9,15}$',
        message="El numero de telefono no es valido"
    )
    phone_number = serializers.CharField(validators=[phone_regex] , max_length=16)
    confirmation_password = serializers.CharField(min_length = 8, max_length = 64)

    def validate(self,data):
        password = data['password']
        confirmation_password = data['confirmation_password']
        if password != confirmation_password:
            raise serializers.ValidationError('Contraseñas no coiciden')
        password_validation.validate_password(password)
        return data

    def create(self, data):
        data.pop('confirmation_password')
        user = User.objects.create_user(**data)
        client = Client.objects.create(user = user)
        return user