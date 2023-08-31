from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email',]

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User 
        exclude = ['password']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance 