from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializerRegister,UserSerializer
from .models import User

class UserView(APIView):
  
  def post(self,request):
    data_user = request.data
    data_user_serialized = UserSerializerRegister(data=data_user)

    if not data_user_serialized.is_valid():
      return Response(
      {
        'ok': False,
        'errors' : data_user_serialized.errors
      },
      status.HTTP_400_BAD_REQUEST
      )

    user_response=data_user_serialized.save()
    user = UserSerializer(user_response)
    
    return Response(
      {
        'ok': True,
        'user' : user.data,
      },
      status.HTTP_200_OK
      )

