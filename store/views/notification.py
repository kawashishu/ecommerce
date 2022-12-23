

from django.http import JsonResponse
from django.shortcuts import redirect
from store.models import Notification


def seen_notifications(request, pk):
    notification = Notification.objects.get(id=pk)
    notification.read = True
    notification.save()
    return redirect(notification.link)
