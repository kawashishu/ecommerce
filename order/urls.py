
from django.urls import path
from . import views


urlpatterns = [
    path('billing/', views.BillingView.as_view() ,name='billing'),

]


