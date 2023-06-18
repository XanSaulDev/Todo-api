from rest_framework.serializers import ModelSerializer

from .models import Todo

class TodoSerializer(ModelSerializer):

  class Meta:
    model = Todo
    fields = ['title','detail','is_completed','id']

class TodoSerializerCreate(ModelSerializer):

  class Meta:
    model = Todo
    fields = '__all__'