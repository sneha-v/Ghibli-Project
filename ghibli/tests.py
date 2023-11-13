from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from dotenv import load_dotenv
import os

load_dotenv()

class ListMoviesTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("list_movies")
    
    def authenticate(self):
        key = os.environ.get('GHIBLI_KEY')
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {key}")

    def test_shouldnot_list_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_list_movies(self):
        self.authenticate()
        response = self.client.get(self.url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), list)