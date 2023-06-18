from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer,TodoSerializerCreate


class TodoView(APIView):


  def get(self,request,*args,**kwargs):
    user = request.user
    todos = Todo.objects.filter(id_owner=user)
    todos_serialized = TodoSerializer(todos,many=True)
    return Response(
    {
      'ok':True,
      'todos': todos_serialized.data
    },
    status.HTTP_200_OK
    )
  
  def post(self,request,*args,**kwargs):
    user = request.user
    todo_data = request.data
    todo_data["id_owner"] = user.id
    data_serialized = TodoSerializerCreate(data=todo_data)
    if not data_serialized.is_valid():
      return Response(
      {
        'ok':False,
        'errors': data_serialized.errors
      },
      status.HTTP_406_NOT_ACCEPTABLE
      )
    data_serialized.save()
    return Response(
    {
      'ok':True,
      'todo': data_serialized.data
    },
    status.HTTP_406_NOT_ACCEPTABLE
    )
