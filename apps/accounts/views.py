from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import UserSerializerRegister,UserSerializer
from .models import User

# TODO: Refactor duplicate code

class UserView(APIView):
  
  def get(self,request,*args,**kwargs):
    user = request.user
    if user.is_anonymous:
      return Response(
      {
        'ok':False,
        'errors': {
          'user': [
            'Usuario no encontrado.'
            ]
        }
      },
      status.HTTP_404_NOT_FOUND
    )

    user_serialized = UserSerializer(user)
    
    return Response(
      {
        'ok':True,
        'user': user_serialized.data
      },
      status.HTTP_200_OK
    )

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
    refresh = RefreshToken.for_user(user_response)
    return Response(
      {
        'ok': True,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user' : user.data,
      },
      status.HTTP_201_CREATED
      )

  def put(self,request,*args,**kwargs):
    user = request.user
    if user.is_anonymous:
      return Response(
      {
        'ok':False,
        'errors': {
          'user': [
            'Usuario no encontrado.'
            ]
        }
      },
      status.HTTP_404_NOT_FOUND
    )
    users_serialized = UserSerializer(user,data=request.data,partial=True)
    if not users_serialized.is_valid():
      return Response(
      {
        'ok': False,
        'errors': users_serialized.error_messages
      },
      status.HTTP_400_BAD_REQUEST
    )
    users_serialized.save()

    return Response(
      {
        'ok': True,
        'user': users_serialized.data
      },
      status.HTTP_200_OK
    )
  
  def delete(self,request,*args,**kwargs):

    user = request.user

    if user.is_anonymous:
      return Response(
      {
        'ok':False,
        'errors': {
          'user': [
            'Usuario no encontrado.'
            ]
        }
      },
      status.HTTP_404_NOT_FOUND
    )


    user.delete()
    
    return Response(
      {
        'ok':True,
        'success': 'Cuenta borrada exitosamente.'
      },
      status.HTTP_200_OK
    )
  
class LoginView(APIView):

  def post(self,request,*args,**kwargs):

    user = authenticate(**request.data)

    if not user:
      return Response({
        'ok':False,
        'errors':['No se encontró ningún usuario con las credenciales proporcionadas.']

      },
      status.HTTP_400_BAD_REQUEST
      )
    
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token
    user_serialized = UserSerializer(user)
    return Response({
      'ok':True,
      'refresh': str(refresh_token),
      'access': str(access_token),
      'user': user_serialized.data
    },
    status.HTTP_200_OK
    )
