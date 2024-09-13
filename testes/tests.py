from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

class UserRegistrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:register_user')  # Ajuste se necessário

    def test_register_user_success(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'securepassword123',
            'email': 'testuser@example.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_user_missing_field(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'securepassword123'
            # 'email' field is missing
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid input data')  # Ajuste conforme a validação

    def test_register_user_duplicate_username(self):
        User.objects.create_user(username='testuser', password='securepassword123', email='testuser@example.com')
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'anotherpassword',
            'email': 'newemail@example.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Username already exists')  # Ajuste conforme a validação
