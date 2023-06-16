from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError

class UserSerializerRegister(serializers.ModelSerializer):
  password_confirm = serializers.CharField()
  class Meta:
    model = User 
    fields = ['email','first_name','last_name','password','password_confirm']
    extra_kwargs = {
      'password' : {'write_only': True},
      'first_name': {'required': True, 'allow_blank': False},
      'last_name': {'required': True, 'allow_blank': False},
    }
  def validate(self,data):
    password = data.get('password')
    password_confirm = data.pop('password_confirm')
    if password != password_confirm:
      raise ValidationError({'password':'Las contraseñas deben coincidir.'})
    return data

  def create (self, validated_data):
      password = validated_data.pop('password')
      try:
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
      except Exception as e:
        return e


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email','first_name','last_name']