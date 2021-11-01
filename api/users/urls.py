from django.urls import path

from api.users.views import UserLoginAPIView, UserSignupAPIView

urlpatterns = [
    path('user/login/', UserLoginAPIView().as_view(), name='login'),
    path('user/signup/', UserSignupAPIView().as_view(), name='signup'),
]
