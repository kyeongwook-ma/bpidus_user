from rest_framework import status
from rest_framework.test import APITestCase


class AccountAPITest(APITestCase):
    def test_signup_api(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.post('/signup', format='json', data={
            'email': 'sample@example.com',
            'password': '21341234123',
            'profile': {
                'name': 'John',
                'nickname': 'Doe',
                'email': 'sample@example.com',
                'phone_number': '010-0000-0000'
            }

        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

