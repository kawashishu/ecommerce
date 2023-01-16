from django.shortcuts import render
from django.shortcuts import HttpResponse
from channels.layers import get_channel_layer


# Create your views here.
# chat/views.py
from django.shortcuts import render

# chat/views.py
from django.shortcuts import render

from asgiref.sync import async_to_sync
def notifications(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications_1",
        {
            "type": "notifications.message",
            "message": "Hello world!",
        },
    )
    return HttpResponse("Notifications sent!")

