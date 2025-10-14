from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class LoginEndpointTest(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_login_returns_tokens(self):
		# create user
		from users.models import User
		email = 'apitest@example.com'
		password = 'testpass123'
		User.objects.create_user(username=email, email=email, password=password)

		url = reverse('login')
		resp = self.client.post(url, {'email': email, 'password': password}, format='json')
		self.assertEqual(resp.status_code, 200, msg=f'Response: {resp.status_code} {resp.content}')
		data = resp.json()
		self.assertIn('access', data)
		self.assertIn('refresh', data)
