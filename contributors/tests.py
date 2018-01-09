from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from .models import Contributor
from defibs.models import Defib

class ListRetrievalTestCase(APITestCase):

    url = reverse('contributor-list')

    def setUp(self):
        self.contributor1 = Contributor.objects.create(name='Alice')
        for i in range(10):
            Defib.objects.create(
                lat=i,
                lon=i,
                contributor=self.contributor1,
            )
        self.contributor2 = Contributor.objects.create(name='Bob')
        for i in range(5):
            Defib.objects.create(
                lat=i,
                lon=i,
                contributor=self.contributor2,
            )
        self.contributor3 = Contributor.objects.create(name='Cathy')
        for i in range(15):
            Defib.objects.create(
                lat=i,
                lon=i,
                contributor=self.contributor3,
            )

    def test_list_retrieval_returns_http_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_retrieval_returns_list(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.data, list)

    def test_list_retrieval_returns_list_of_expected_length(self):
        expected_length = Contributor.objects.all().count()
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), expected_length)

    def test_list_is_ordered_by_number_of_defibs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data[0]['name'], self.contributor3.name)
        self.assertEqual(response.data[1]['name'], self.contributor1.name)
        self.assertEqual(response.data[2]['name'], self.contributor2.name)

    def test_list_object_contains_expected_fields(self):
        response = self.client.get(self.url)
        c = response.data[0]
        self.assertEqual(
            set(['name', 'defib_count']),
            set(c.keys()),
        )

    def test_list_object_contains_correct_data(self):
        response = self.client.get(self.url)
        c = response.data[0]
        self.assertEqual(
            c['defib_count'],
            Defib.objects.filter(contributor=self.contributor3).count(),
        )
