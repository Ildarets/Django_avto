from django.test import TestCase
from .models import Avto, Marks, Mesto
from usersapp.models import BlogUser
from faker import Faker
from mixer.backend.django import mixer


class PostTestCaseMixer(TestCase):

    def setUp(self):
        self.post = mixer.blend(Avto)


    def test_has_image(self):
        self.assertFalse(self.post.has_image())


