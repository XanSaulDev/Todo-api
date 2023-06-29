

from django.urls import include, path

urlpatterns = [
  path('todos',include('TODOS.urls')),
  path('users/',include('accounts.urls'))
]