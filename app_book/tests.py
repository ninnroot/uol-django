from rest_framework.test import APITestCase

import json

from django.core.management import call_command
from django.urls import reverse


class AppBookTest(APITestCase):

    def setUp(self) -> None:
        call_command("migrate")
        call_command("load-data")

    def login(self, email: str="superadmin@dad-lib.com"):
        response = self.client.post(
            reverse("login"),
            {
                "email": email,
                "password": "Password123$",
            },
        )
        return response.data["access"]


    def test_book_get(self):
        response = self.client.get(
            reverse("book-list"),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 200)

    def test_book_create(self):
        response = self.client.post(
            reverse("book-list"),
            json.dumps({"title": "Test", "author": 1}),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 201)

    def test_book_get(self):
        response = self.client.get(
            reverse("book-list"),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 200)

    def test_book_create(self):
        response = self.client.post(
            reverse("book-list"),
            json.dumps({"title": "Test", "author": 1}),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 201)

    def test_author_get(self):
        response = self.client.get(
            reverse("author-list"),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 200)

    def test_author_create(self):
        response = self.client.post(
            reverse("author-list"),
            json.dumps({"name": "Test"}),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 201)

    def test_genre_get(self):
        response = self.client.get(
            reverse("genre-list"),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 200)

    def test_genre_create(self):
        response = self.client.post(
            reverse("genre-list"),
            json.dumps({"name": "Test",}),
            content_type="application/json",
            HTTP_AUTHORIZATION=f"Bearer {self.login()}"
        )
        self.assertEquals(response.status_code, 201)