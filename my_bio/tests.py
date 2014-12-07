import os
from django.core.files.images import ImageFile
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.contrib.auth.models import User
from my_bio.models import MyBio, HttpRequestSave


class BioTests(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('temporary',
                                 'temporary@temporary.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

    def test_bio_model(self):
        bio = MyBio(first_name='Oleksii', last_name='Aledinov')
        self.assertEquals(
        str(bio),
        'Bio data for Oleksii Aledinov',
        )

    def test_bio_in_the_context(self):
        response = self.client.get('/')
        self.assertEquals(list(response.context['bio_list']), [])
        with open(os.path.join(settings.MEDIA_ROOT, "foto.png"), 'rb') \
                 as img_file_read:
            image_file = ImageFile(img_file_read.read())
            MyBio.objects.create(first_name='Oleksii', last_name='Aledinov',
                                  photo=image_file)
            response = self.client.get('/')
            self.assertEquals(response.context['bio_list'].count(), 1)

    def test_bio_edit(self):
        with open(os.path.join(settings.MEDIA_ROOT, "foto.png"), 'rb') \
                as img_file_read:
            image_file = ImageFile(img_file_read.read())
            bio_object = MyBio.objects.create(first_name='Oleksii',
                                              last_name='Aledinov',
                                              photo=image_file)
            response = self.client.get('/edit/{0}/'.format(bio_object.id))
            self.assertEquals(response.context['bio'].first_name,
                              bio_object.first_name)


class RequestMiddlewareTests(TestCase):

    def test_requests(self):
        client = Client()
        client.get('/')
        req_list = HttpRequestSave.objects.all()
        self.assertEquals(req_list.count(), 1)


class ContextTest(TestCase):

    def test_settings_processor(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.context['settings'], settings)
