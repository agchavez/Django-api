from django.urls import path
from django.urls.conf import include

from api.circles.views import list_circles

urlpatterns = [
    path('circles/', list_circles)
]
