from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from customer.form import RegistrationForm, UpdateProfileForm

class TestForm(TestCase):
    def test_registration_form(self):
        form = RegistrationForm(data={
            'name': 'testName',
            'phone': '123456789',
            'email': 'testEmail@gmail.com',
            'password': 'testPassword',
            'confirm_password': 'testPassword',
            'captcha': 'testCaptcha',
        })

        self.assertTrue(form.is_valid())

    def test_update_profile_form(self):
        form = UpdateProfileForm(data={
            'name': 'testName',
            'phone': 'testPhone',
            
        })

        self.assertTrue(form.is_valid())