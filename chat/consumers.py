import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.room_name =self.scope['url_route']['kwargs']['room_name']
            self.room_group_name=self.scope='chat_%s'%self.room_name
            # self.accept()
            # self.send
            
            # Join room group
            await self.channel_layer.group_add(self.room_group_name,self.channel_name)
            await self.accept()
        except Exception as e:
            print(e)    
    async def receive(self, text_data=None):
        # await self.channel_layer.groupsend
        # print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
        