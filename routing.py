from django.core.asgi import get_asgi_application
from channels.generic.websocket import WebsocketConsumer

application = get_asgi_application()

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data='You have a new notification: {}'.format(text_data))