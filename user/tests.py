from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .services import *


class UserTests(TestCase):
    def test_create_user_service(self):
        """
        create_user() should return False for future publication dates.
        """
        result = create_user(_name='John', _nickname='Doe', _phone_number='010-0000-0000')
        self.assertEqual(result, True)


class AccountTests(APITestCase):
    def test_create_account_api(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.post('/users/', format='json', data={
            'name': 'John',
            'nickname': 'Doe',
            'phone_number': '010-0000-0000'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
