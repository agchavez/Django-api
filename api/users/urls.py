from django.urls import path

from api.users.views import UserLoginAPIView

urlpatterns = [
    path('user/login/', UserLoginAPIView().as_view(), name='login'),
]
