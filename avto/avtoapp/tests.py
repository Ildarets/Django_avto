from django.test import TestCase
from .models import Avto, Marks, Mesto
from usersapp.models import BlogUser
from faker import Faker
from mixer.backend.django import mixer


class AvtoTestCaseMixer(TestCase):

    def setUp(self):
        self.post = mixer.blend(Avto)


    def test_has_image(self):
        self.assertFalse(self.post.has_price())


class MarksTestMixer(TestCase):
    def setUp(self):
        self.marka = Marks.objects.create(name = 'test_name')

    def test_str(self):
        self.assertEqual(str(self.marka), 'test_name')
    #


class MestoTestMixer(TestCase):
    def setUp(self):
        self.marka = Mesto.objects.create(name='test_name_mesto')

    def test_str(self):
        self.assertEqual(str(self.marka), 'test_name_mesto')
