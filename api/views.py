from django.shortcuts import render
from rest_framework import generics
from .models import *
from django.db.models import Q,Prefetch 
from .serializer import *
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

def if_integer(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

@permission_classes((IsAuthenticated,))
class userList(APIView):
    def get(self,request,*args, **kwargs):
        """
        return user
        """
        user_document=kwargs["user_document"]
        if(not if_integer(user_document)):
            return Response({'details':'no es entero'},status=status.HTTP_400_BAD_REQUEST)
        user = Users.objects.filter(user_document=user_document)
        if(user.exists()):
            users = userSerializer(user,many=True)
            return Response(users.data,status=status.HTTP_200_OK)
        else:
            return Response({'details':'no se encuentra usuario'},status=status.HTTP_404_BAD_REQUEST)

@permission_classes((AllowAny,))   
class getToken(APIView):
    def get(self, request):
        texto_inicio = "login"
        url = render(request, "backend/templates/login.html", context={'texto_inicio':texto_inicio})
        return url