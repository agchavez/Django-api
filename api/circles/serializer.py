""" Clase de serialize para circulos"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#models
from api.circles.models import Circles

class CircleSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_offered = serializers.IntegerField()
    rides_taken = serializers.IntegerField()
    member_limit = serializers.IntegerField()
    created = serializers.DateTimeField()

class CreateCircleSerializer(serializers.Serializer):
    name= serializers.CharField()
    slug_name = serializers.SlugField(
        validators=[UniqueValidator(queryset=Circles.objects.all())]
    )
    about = serializers.CharField(
        max_length = 250,
        required = False
    )

    def create(self, data):
        return Circles.objects.create(**data)