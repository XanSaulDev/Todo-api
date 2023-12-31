from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Todo
from .serializers import TodoSerializer,TodoSerializerCreate

class TodoView(APIView):
  permission_classes = [IsAuthenticated]
  todos_per_page = 10
  
  def get(self,request,*args,**kwargs):
    user = request.user

    todos = Todo.objects.filter(id_owner=user.id)

    paginator = Paginator(todos,self.todos_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    todos_serialized = TodoSerializer(page_obj.object_list,many=True)

    return Response(
      {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'todos': todos_serialized.data,
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
    todo = data_serialized.save()
    todo_serialized = TodoSerializer(todo)
    return Response(
    {
      'ok':True,
      'todo': todo_serialized.data
    },
    status.HTTP_201_CREATED
    )

  def put(self,request,*args,**kwargs):
    user = request.user
    id_todo = request.data.get('id')
    todo = Todo.objects.filter(id_owner=user).filter(id=id_todo).first()
    todo_serialized = TodoSerializer(todo,data=request.data,partial=True)
    if not todo_serialized.is_valid():
      return Response({
        'ok': False,
        'errors': todo_serialized.errors
      },status.HTTP_400_BAD_REQUEST)
    todo_serialized.save()
    return Response({
      'ok': True,
      'todo': todo_serialized.data
    },status.HTTP_202_ACCEPTED)
  
  def delete(self,request,*args,**kwargs):
    user = request.user
    id_todo = request.data.get('id')
    todo = Todo.objects.filter(id_owner=user).filter(id=id_todo).first()
    if not todo:
      return Response({
        'ok': False,
        'errors': ['Todo no encontrado.']
      },status.HTTP_202_ACCEPTED)
    
    todo.delete()
    return Response({
      'ok': True,
      'success': 'Todo eliminado correctamente.'
    },status.HTTP_202_ACCEPTED)
  

class SearchTodo(APIView):
  todos_per_page = 10

  def post(self,request,*args,**kwargs):
    user = request.user

    if request.data.get('search'):
      
      todos = Todo.objects.filter(  Q(title__icontains=request.data.get('search')) | 
                                    Q(detail__icontains=request.data.get('search'))).filter(id_owner=user.id)

      data_serialized = TodoSerializer(todos,many=True)

      return Response(
        {
        'ok': True,
        'todos': data_serialized.data
        },
        status.HTTP_200_OK
      )
    
    todos = Todo.objects.filter(id_owner=user.id)
    paginator = Paginator(todos,self.todos_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    todos_serialized = TodoSerializer(page_obj.object_list,many=True)
    return Response(
      {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'todos': todos_serialized.data,
      },
    status.HTTP_200_OK
    )