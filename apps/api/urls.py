

from django.urls import include, path

urlpatterns = [
  path('todos',include('apps.TODOS.urls')),
  path('users',include('apps.accounts.urls'))
]