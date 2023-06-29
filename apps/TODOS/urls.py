from django.urls import path, include
from .views import TodoView,SearchTodo

urlpatterns = [
  path('',TodoView.as_view()),
  path('/search-todo',SearchTodo.as_view())
]