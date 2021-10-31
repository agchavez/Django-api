#Django-rest-framwork
from rest_framework.decorators import api_view
from rest_framework.response import Response
#modesl 
from api.circles.serializer import CircleSerializer, CreateCircleSerializer
from api.circles.models import Circles

@api_view(['GET'])
def list_circles(request):
    #Retornar todos los circulos
    circles = Circles.objects.filter(public = True)
    serializer = CircleSerializer(circles, many=True )
    return Response(serializer.data)

@api_view(['POST'])
def add_circle(request):
    #Crear nuevo circulo 
    serializers = CreateCircleSerializer(data=request.data)
    #raise_exception , Retrnar errores automaticamente
    serializers.is_valid(raise_exception=True)
    circle = serializers.save()
    return Response(CircleSerializer(circle).data)
