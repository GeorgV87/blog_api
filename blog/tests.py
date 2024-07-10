from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Post, Comment

# Create your tests here.

class BlogAPITests(TestCase):
    # Stuff we need for every test...
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = Client()
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {self.token.key}'
