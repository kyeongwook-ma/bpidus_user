from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User


class UserAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(id='7bc3c004-05d6-4d4d-a70b-cf0507320784', name="user1",
                            email='sample@example.com',
                            nickname="u1", phone_number='010-0000-0000')

    def test_get_user_api(self):
        """
        Ensure we can create a new account object.
        """
        response = self.client.get('/users/7bc3c004-05d6-4d4d-a70b-cf0507320784/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
