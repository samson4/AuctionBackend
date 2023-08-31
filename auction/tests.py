import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory,force_authenticate
from rest_framework import status
from django.urls import reverse
import uuid
from. models import Auction,Lot
from Users.models import User
from Users.serializers import UserSerializer
from . import views
from .serializers import AuctionSerializer,LotSerializer
# Create your tests here.
class AuctionTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.AuctionView().as_view()
        self.auction = Auction.objects.create(title='testlot')
        self.serializer = AuctionSerializer
    def test_auction_exists_view(self):
        url = reverse('auction')
        request = self.factory.get(url)  
        response = self.view(request)
        

        self.assertEqual(response.status_code,status.HTTP_200_OK)

        self.assertEqual(Auction.objects.count(),1)

        test_serializer  = self.serializer([self.auction],many=True)
        
        self.assertEqual(response.data,test_serializer.data)

    def test_auction_create_view(self):
        url = reverse('auction')
        valid_data = {'title':'demoAuctiontitle'}
        request = self.factory.post(url,valid_data)
        
        response = self.view(request)
       
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual({'id':response.data['id'],'lot_count':0,'title':'demoAuctiontitle','subscribers':[]},response.data)
    
    def test_auction_detail_view(self):
        url = reverse('auction-detail',kwargs={'id':self.auction.id})
        request = self.factory.get(url)
        response = views.AuctionDetailView.as_view()(request,id=self.auction.id)
        expected_output = AuctionSerializer(self.auction)
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,expected_output.data)


class LotTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.LotView.as_view()
        self.serializer = LotSerializer
        self.auction = Auction.objects.create(title='testauction2')
        self.lot = Lot.objects.create(title='testlot2',description='test lot description',condition='Used',Price='1200.00')  
        self.auction.lots = self.lot
        
  
    def test_lot_create_view(self):
        url = reverse('create-lots',kwargs={'id':self.auction.id})
        self.view = views.LotCreateView.as_view()
       
        validated_data = {
            'title':'test lot create view title',
            'description':'test lot create view description',
            'condition':'Used',
            'Price' :'1200'
        }
        request = self.factory.post(url,validated_data,format='json')
        
        response = self.view(request,id=self.auction.id)
        
        expected_output = {
            
            'title':'test lot create view title',
            'description':'test lot create view description',
            'condition':'Used',
            'Price' :'1200',
            'auction':self.auction,
        }
        test_serializer = LotSerializer(expected_output)
        
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) 
        self.assertEqual(response.data,test_serializer.data) 
          
class SubscriptionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'testuser',email='testemail@gmail.com',password='123456')
        self.auction = Auction.objects.create(title='testauction')
        self.view = views.AuctionSubscribeView.as_view()
        self.factory= APIRequestFactory()

    def test_user_subscribes_auction_view(self):
        url = reverse('auction-subscribe',kwargs={'id':self.user.id})
        request = self.factory.post(url)
        force_authenticate(request,user=self.user)
        response = self.view(request,id=self.auction.id)
        expected_output = {
            "lot_count":0,
            "title":"testauction",
            "subscribers":[(self.user.id)]
        }
        print('response',response.data)

        test_serializer = AuctionSerializer(expected_output,many=True)
        print('expected',test_serializer.data)
        

        