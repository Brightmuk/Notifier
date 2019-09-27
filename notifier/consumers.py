import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NoseyConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('gossip',self.channel_name)
        print(f'Added {self.channel_name} to gossip')

    async def disconnect(self):
        await self.channel_layer.group_discard('gossip',self.channel_name)
        print(f'Discarded {self.channel_name} from gossip')

    async def user_gossip(self, event):
        await self.send_json(event)
        print(f'Got message {event} at {self.channel_name}')