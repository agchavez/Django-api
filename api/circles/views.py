#Django 
from django.http import JsonResponse

#modesl 
from api.circles.models import Circles, circles
def list_circles(request):
    circles = Circles.objects.all()
    public = circles.filter(public = True)
    data = []
    for circle in public:
       data.append( {
            'name':circle.name,
            'slug_name':circle.slug_name,
            'rides_taken':circle.rides_taken,
            'rides_offered':circle.rides_offered,
            'member_limit':circle.member_limit,
        })
        
    return JsonResponse(data, safe=False)