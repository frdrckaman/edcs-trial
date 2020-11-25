from django.test import TestCase, Client
from django.urls import reverse
from .factory import UserFactory


class TestApp(TestCase):
    def test_user_authentication(self):
        client = Client()
        user = UserFactory()
        client.force_login(user)
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_unauthenticated_access(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 302)


