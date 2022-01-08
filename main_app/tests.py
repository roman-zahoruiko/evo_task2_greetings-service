from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from .models import UserData
from .forms import UserDataForm
from .views import index


class TestForms(SimpleTestCase):
    def test_user_data_form(self):
        form = UserDataForm(data={"data": "JOHN SMITH"})
        self.assertTrue(form.is_valid())


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
        self.data = UserData.objects.create(data='John')

    def test_index_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main_app/index.html")

    def test_index_new_data(self):
        response = self.client.post(self.url, data={'data': 'Jekos'})
        self.assertEqual(response.context.get('message'), 'Hello, dear Jekos!')
        self.assertEqual(response.status_code, 200)

    def test_index_greeted_data(self):
        response = self.client.post(self.url, data={'data': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('message'), "We've already met, dear John!")

    def test_index_greeted_list(self):
        response = self.client.post(self.url, data={'greeted_list': ''})
        greeted_user = response.context.get('greeted_list').values_list()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(greeted_user[0][1], 'John')
