from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import BlogUser

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()


    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/avto_list/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 302)

        # post зарос
        response = self.client.post('/contact/',
                                    {'name': self.fake.name(), 'message': self.fake.text(),
                                     'email': self.fake.email()})

        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertTrue('avto' in response.context)


    def test_login_required(self):
        BlogUser.objects.create_user(username='ildar', email='test@test.com', password='9205466309')

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)

        # Логиним
        self.client.login(username='ildar', password='9205466309')

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)