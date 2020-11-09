
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode


class BaseTest(TestCase):
    def setUp(self):
        self.login_url=reverse('loginuser')
        self.signup_url=reverse('signupuser')
        self.current=reverse('currenttodos')
        User.objects.create_user('test_user', password='12345678')
        self.user={
            'username':'test_user',
            'password':'12345678',
        }
        self.client = Client()
        return super().setUp()


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/login.html')

    def test_login_success(self):
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cantlogin_with_no_username(self):
        response = self.client.post(self.login_url, {'password': 'passwped', 'username': ''}, format='text/html')
        self.assertEqual(response.status_code, 402)
        self.assertTemplateUsed(response, 'todo/login.html')

    def test_cantlogin_with_no_password(self):
        response = self.client.post(self.login_url, {'username': 'passwped', 'password': ''}, format='text/html')
        self.assertEqual(response.status_code, 402)
        self.assertTemplateUsed(response, 'todo/login.html')


class SignUp(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/signupuser.html')

    def test_signup_success(self):
        datos = {
            'username': 'test_user3',
            'password1': '123456789',
            'password2': '123456789'
        }
        response = self.client.post(self.signup_url, datos, format='text/html')
        self.assertEqual(response.status_code, 302)
