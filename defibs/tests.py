from django.conf import settings
from django.core import mail
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from defibs.models import Defib

# Create your tests here.
class ListRetrievalTestCase(APITestCase):

    url = reverse('defib-list')

    def setUp(self):
        # Create some defibs
        for i in range(10):
            Defib.objects.create(lat=i, lon=i)

    def test_list_retrieval_returns_http_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_retrieval_returns_list(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.data, list)

    def test_list_retrieval_returns_list_of_expected_length(self):
        expected_length = Defib.objects.all().count()
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), expected_length)


class DetailRetrievalTestCase(APITestCase):

    def setUp(self):
        self.defib = Defib.objects.create(lat=0, lon=0)
        self.url = reverse('defib-detail', args=[self.defib.id])

    def test_detail_retrieval_returns_http_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_retrieval_returns_object(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.data, object)

    def test_detail_retrieval_returns_expected_keys(self):
        expected_keys = set([
            'id', 'lat', 'lon', 'notes', 'address', 'image',
        ])
        response = self.client.get(self.url)
        self.assertEqual(set(response.data.keys()), expected_keys)


class SubmissionTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'lat': 0,
            'lon': 0,
        }
        self.url = reverse('defib-submit')

    def test_submission_returns_http_201(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_submission_triggers_an_email(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(len(mail.outbox), 1)

    def test_submission_email_sends_to_expected_recipient(self):
        expected_recipient = settings.SUBMISSION_EMAIL_TO
        response = self.client.post(self.url, self.data)
        sent_mail = mail.outbox[0]
        self.assertEqual(sent_mail.to[0], expected_recipient)

    def test_missing_data_returns_http_400(self):
        data = {'lat': 0}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
