from django.urls import path
from django.urls.conf import include

from api.circles.views import list_circles,add_circle

urlpatterns = [
    path('circles/', list_circles),
    path('circles/create/', add_circle),
]
