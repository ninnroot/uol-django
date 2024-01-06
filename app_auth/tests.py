import json
from rest_framework.test import APITestCase

from django.core.management import call_command
from django.urls import reverse


class UserTest(APITestCase):

    def setUp(self) -> None:
        call_command("migrate")
        call_command("load-data")

    def test_login(self):

        response = self.client.post(
            reverse("login"),
            {
                "email": "superadmin@dad-lib.com",
                "password": "Password123$",
            })

        print(response.content)
        self.assertEquals(response.status_code, 200)
