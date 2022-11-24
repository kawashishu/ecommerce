from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.ContactView.as_view() ,name='contact'),
]
