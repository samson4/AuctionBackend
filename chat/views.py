from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
import json
# Create your views here.
@api_view(['POST'])
def create_room(request,uuid):
    name = request.data['name']
    url = request.data['url']

    Room.objects.create(uuid=uuid,client=name,url=url)

    return Response({'message':'room created'})
