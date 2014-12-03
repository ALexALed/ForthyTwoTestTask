from django.test import TestCase
from django.test.client import Client
from my_bio.models import MyBio

class BioTests(TestCase):

    def test_bio_model(self):
        bio= MyBio(first_name='Oleksii', last_name='Aledinov')
        self.assertEquals(
        str(bio),
        'Bio data for Oleksii Aledinov',
        )

    def test_bio_in_the_context(self):
         client = Client()
         response = client.get('/')
         self.assertEquals(list(response.context['bio_list']), [])
         MyBio.objects.create(first_name='Oleksii', last_name='Aledinov')
         response = client.get('/')
         self.assertEquals(response.context['bio_list'].count(), 1)
