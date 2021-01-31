from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

class AccountsTest(APITestCase):
    def setUp(self):
        # we want to go ahead and orginally create a user
        self.test_user = User.objects.create_user('testuser','test@example.com','testpassword')
        # URL for creating an account.
        self.create_url = reverse('account-create')

        def test_create_user(self):
            """
            Ensure we can create a new user and a valid token is create with it.
            """
            data = {
                'username':'foobar',
                'email':'foobar@example.com',
                'password':'somepassword'
            } 
            response = self.client.post(self.create_url, data, format='json')
            # We want to make user we have two users in the database..
            self.assertEqual(User.objects.count(), 2)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Additionally, we want to return the username and email upon successful creation.

            self.assertEqual(response.data['username'], data['username'])
            self.assertEqual(response.data['email'], data['email'])
            self.assertFalse('password' in response.data)
            

# Create your tests here.
