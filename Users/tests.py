from django.test import TestCase
from rest_framework.test import APIRequestFactory,force_authenticate
from rest_framework import status
from django.urls import reverse
from . import views
from .models import User
# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.factory =APIRequestFactory()
        self.view = views.Register.as_view()
    def test_user_create_view(self):
        url = reverse('register')
        user_data={
            'username':'testuser',
            'email':'testuser@gmail.com',
            'password' : '123456'
        }
       
        request = self.factory.post(url,user_data)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data,{'username':'testuser',
            'email':'testuser@gmail.com',})
        
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'testuser',email='testemail@gmail.com',password='123456')
        self.factory = APIRequestFactory()
        self.view = views.Profile.as_view()
    def test_user_retrieve_view(self):
        url=reverse('user-profile') 
        request = self.factory.get(url)
        force_authenticate(request,user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_user_update_view(self):
        url=reverse('user-profile') 
        valid_data={
            'username':'testuser2',
            'email':'testemail2@gmail.com'
        } 
        request = self.factory.put(url,valid_data)
        # print(request)
        force_authenticate(request,user=self.user)
         
        response = self.view(request)
        print(response.data)  