
from django.urls import path
from . import views
import admin_notifications


urlpatterns = [
    path('billing/', views.BillingView.as_view() ,name='billing'),

]


