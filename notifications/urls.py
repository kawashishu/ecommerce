# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("send_notifications/", views.notifications, name="send_notifications")
]