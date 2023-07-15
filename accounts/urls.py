

from django.urls import path
from .views import UserView,LoginView,RegisterView

urlpatterns = [ 
  path('',UserView.as_view()),
  path('<int:id>',UserView.as_view()),
  path('login',LoginView.as_view()),
  path('register',RegisterView.as_view()),

]