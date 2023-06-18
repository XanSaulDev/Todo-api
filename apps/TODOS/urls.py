from django.urls import path, include
from .views import TodoView

urlpatterns = [
  path('',TodoView.as_view())
]