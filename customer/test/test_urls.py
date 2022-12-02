from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ecommerce.views import Index, message_processor
from customer.views import login, api, password

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, Index)
    
    def register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, login.RegistrationView)
        
    def login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, login.LoginView)
        
    def logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, login.logout)
        
    def activate_url_is_resolved(self):
        url = reverse('activate')
        self.assertEquals(resolve(url).func.view_class, login.activate)
        
    def profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, login.ProfileView)
    
    def forgot_password_url_is_resolved(self):
        url = reverse('forgot_password')
        self.assertEquals(resolve(url).func.view_class, password.forgotPassword)
        
    def reset_password_validate_url_is_resolved(self):
        url = reverse('reset_password_validate')
        self.assertEquals(resolve(url).func.view_class, password.reset_password_validate)
        
    def reset_password_url_is_resolved(self):
        url = reverse('reset_password')
        self.assertEquals(resolve(url).func.view_class, password.reset_password)
        