# chat/routing.py
from django.urls import re_path

from notifications.consumers import consumers_notifications

websocket_urlpatterns = [
    re_path(r"ws/notifications/(?P<room_name>\w+)/$", consumers_notifications.NotificationsConsumer.as_asgi()),
]