from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from .serializers import UserSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):

  def validate(self,attrs):
    data = super().validate(attrs)
    refresh = self.get_token(self.user)
    
    data['ok'] = True
    data['refresh'] = str(refresh)
    data['access'] = str(refresh.access_token)
    
    data['user'] = UserSerializer(self.user).data

    return data

class CustomTokenResponse(TokenObtainPairView):
  serializer_class = CustomTokenSerializer