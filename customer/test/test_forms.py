
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve

from customer.form import RegistrationForm, UpdateProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile

class TestForm(TestCase):
    def setUp(self):
        self.formRegistation = RegistrationForm(data={
            'name': 'testName',
            'phone': '123456789',
            'email': 'testEmail@gmail.com',
            'password': 'testPassword123',
            'confirm_password': 'testPassword123',
            'captcha': 'PASSED',
        })
        self.formUpdate = UpdateProfileForm(data={
            'name': 'testName',
            'phone': '123456',
            'address': 'testAddress',
            'avatar': SimpleUploadedFile('test_avatar.jpg', content=b'', content_type='image/jpeg'),
        })
        self.client = Client()
    
        
        
    def test_registration_form(self):
        assert self.formRegistation.is_valid() == False
       
    def test_update_profile_form(self):
        assert self.formUpdate.is_valid() == False

    def test_update_profile_post(self):
        self.form = self.client.post(reverse('profile'), self.formUpdate)
        assert self.form.status_code == 200
        
        