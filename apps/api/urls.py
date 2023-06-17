

from django.urls import include, path

urlpatterns = [
  path('todos/',include('apps.todos.urls')),
  path('users/',include('apps.accounts.urls'))
]