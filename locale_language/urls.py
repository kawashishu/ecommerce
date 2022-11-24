from django.urls import path, include
from . import views

app_name = 'locale_language'

urlpatterns = [
    path('', views.home, name='translate'),
]