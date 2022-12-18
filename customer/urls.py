from django.urls import include, path
from customer.views import login, api, password


urlpatterns = [

    # login social
    path ('oauth /', include ('social_django.urls', namespace = 'social')),

    # login views
    path('signup/', login.RegistrationView.as_view(), name='signup'),
    path('signin/', login.LoginView.as_view(), name='signin'),
    path('signout/', login.logout, name='signout'),
    path('activate/<uidb64>/<token>', login.activate, name='activate'),
    path('dashboard/', login.ProfileView, name='dashboard'),
    # path('dashboard-edit-profile/', login.ProfileEditView.as_view(), name='dashboard-edit-profile'),
    # path('dashboard-order/', login.OrderView.as_view, name='dashboard-order'),

    # password views
    path('forgot_password/', password.forgotPassword, name = 'forgot_password'),
    path('reset_password_validate/<uidb64>/<token>', password.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', password.reset_password, name='reset_password'),

    #update profile

]