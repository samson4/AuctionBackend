from typing import Any
from django import http
from django.http import Http404
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Auction,Lot
from .serializers import AuctionSerializer,LotSerializer,SubscribedAuctionsSerializer,AuctionDetailSerializer
from Users.serializers import UserSerializer

from Users.models import User
# Create your views here.

class LotView(APIView):
    def get_object(self,id):
        try:
            queryset = Lot.objects.get(pk=id)
            print(queryset)
            serializer = LotSerializer(queryset)
            return Response(serializer.data)
        except Lot.DoesNotExist:
            raise Http404 
    def get(self,request,id):
        return self.get_object(id=id) 
class LotsListView(APIView):
    def get_object(self,id):
        try:
            return Lot.objects.filter(auction__id=id)
        except Lot.DoesNotExist:
            return Http404

    def get(self,request,id):
        serializer = LotSerializer(self.get_object(id=id),many=True)
        return Response(serializer.data)
class LotCreateView(APIView):
    def get_object(self,id):
        try:
            return Auction.objects.get(pk=id)
        except Auction.DoesNotExist:
            raise Http404  

    def post(self,request,id):
          auction = self.get_object(id)
          title = request.data['title']
          description = request.data['description']
          condition = request.data['condition']
          price = request.data['Price']
          LotQuery = Lot.objects.create(title=title,auction=auction,description=description,condition=condition,Price = price)
          
          serializer = LotSerializer(LotQuery)
          return Response (serializer.data,status=status.HTTP_201_CREATED)      
    
class AuctionView(APIView):
    def get_object(self):
        try:
            queryset = Auction.objects.all()
            return queryset
        except Auction.DoesNotExist:
            raise Http404 
        
    def get(self,request):
        queryset = self.get_object()
        serializer = AuctionSerializer(queryset,many=True,context={'request': request,})
        return Response(serializer.data)
    
    def post(self,request):
        title  = request.data['title']
        queryset = Auction.objects.create(title=title)
        serializer = AuctionSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class AllSubscribedAuctionsView(APIView):
    permission_classes=[IsAuthenticated]
    def get_object(self,id):
        try:
            return Auction.objects.filter(subscribers__id = id) 
        except Auction.DoesNotExist:
            raise Http404
    def get(self,request):
        queryset = self.get_object(id=request.user.id)  
        serializers = SubscribedAuctionsSerializer(queryset,many=True,context={'request': request,})
        return Response(serializers.data) 
    
class AuctionDetailView(APIView):
    def get_object(self,id):
        try:
            return Auction.objects.get(pk = id)
        except Auction.DoesNotExist:
            raise Http404

    def get(self,request,id):
        auctionQuery = self.get_object(id=id)
        
        serializer = AuctionDetailSerializer(auctionQuery,context={'request': request})
        return Response(serializer.data)     

class AuctionSubscribeView(APIView):
    
    # authentication_classes=[to]
    # authorization
    permission_classes=[IsAuthenticated]
    def get_object(self,id):
        try:
            return Auction.objects.get(pk=id)
        except Auction.DoesNotExist:
            return Http404
    # def get_user(self,id,user):
    #         return Auction.objects.get(pk=id)  

    # def get(self,request,id):
    #     print(request.user) 
    #     return None          
    def post(self,request,id):
        print('user',(request.user))
        auction = self.get_object(id=id)
        

        # add many to many r/ship b/n user and auction
        auction.subscribers.add(request.user.id)
        
        serializer = SubscribedAuctionsSerializer(auction,context={'request': request})
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,id):
        auction = self.get_object(id=id)
        
        auction.subscribers.remove(request.user.id)
        return Response('Unsubscibed from %s' %id)
