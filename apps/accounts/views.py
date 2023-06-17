from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializerRegister,UserSerializer
from .models import User

class UserView(APIView):
  
  def get(self,request,*args,**kwargs):
    
    user_id = kwargs.get('id')

    if not user_id:
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
    user = User.objects.filter(id=user_id).first()

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
    
    return Response(
      {
        'ok': True,
        'user' : user.data,
      },
      status.HTTP_200_OK
      )

  def put(self,request,*args,**kwargs):
    user = User.objects.filter(id=request.data.get('id')).first()
    print(user)
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
    user_id = kwargs.get('id')

    if not user_id:
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

    user = User.objects.filter(id=user_id).first()

    user.delete()
    
    return Response(
      {
        'ok':True,
        'success': 'Cuenta borrada exitosamente.'
      },
      status.HTTP_200_OK
    )