from django.db import models
from apps.accounts.models import User
# Create your models here.

class Todo(models.Model):
  id_owner = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=50,blank=False)
  detail = models.CharField(max_length=250,blank=True,null=True,default="")
  is_completed = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.title} {self.id_owner}'