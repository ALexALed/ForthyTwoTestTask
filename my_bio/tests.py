from django.test import TestCase
from django.test.client import Client
from my_bio.models import Bio

class BioTests(TestCase):
    def test_bio_in_the_context(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(list(response.context['bio_list']), [])
        Bio.objects.create(first_name='Oleksii', last_name='bar')
        response = client.get('/')
        self.assertEquals(response.context['bio_list'].count(), 1)
