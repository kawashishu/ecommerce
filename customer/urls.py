from django.urls import include, path
from customer.views import login, api, password
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('customer', api.CustomerViewSet, basename='customer')

urlpatterns = [
    # api
    path('api/', include(router.urls)),

    # login social
    path ('oauth /', include ('social_django.urls', namespace = 'social')),

    # login views
    path('register/', login.RegistrationView.as_view(), name='register'),
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.logout, name='logout'),
    path('activate/<uidb64>/<token>', login.activate, name='activate'),
    path('profile/', login.ProfileView.as_view(), name='profile'),

    # password views
    path('forgot_password/', password.forgotPassword, name = 'forgot_password'),
    path('reset_password_validate/<uidb64>/<token>', password.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', password.reset_password, name='reset_password'),

    #update profile

]