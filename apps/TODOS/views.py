from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Test(APIView):
  
  def get(self,request,*args,**kwargs):
    return Response({
      'ok': True
    },status.HTTP_200_OK)
