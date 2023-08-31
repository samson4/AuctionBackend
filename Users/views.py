from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .serializers import UserSerializer,UserProfileSerializer
from .models import User
# Create your views here.

@api_view(['GET'])
def index(request):
    if request.user.is_authenticated:
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)
    else:
        return Response({
    "detail": "Authentication credentials were not provided."
})

class Profile(APIView):
    permission_classes=[IsAuthenticated]
    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Http404
        
    def get(self,request):
        queryset=self.get_object(id=request.user.id)
        
        serializer = UserProfileSerializer(queryset)  
        return Response(serializer.data)
    

    def put(self,request):
    # print(request.data['username'])
        try:
            queryset=self.get_object(id=request.user.id)
            serializer = UserProfileSerializer(queryset,data=request.data)
            if serializer.is_valid(raise_exception=True):
                print('valid')
                serializer.update(instance=queryset,validated_data=request.data)
                return Response(serializer.data)
            else:
                print('invalid')
                return Response(status=status.HTTP_400_BAD_REQUEST)    
        except Exception as e:
            return Response('Username or Email already taken')   


class Register(APIView):
   
    def post(self,request):
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(request.data)
            if user:
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)    

