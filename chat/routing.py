from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/socket-server/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
]