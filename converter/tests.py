from django.test import TestCase
from django.urls import reverse, resolve

class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_weightconverter_page_status_code(self):
        response = self.client.get('/weight_converter/')
        self.assertEqual(response.status_code, 200)

    def test_url_home_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')

    def test_url_weightconverter_by_name(self):
        response = self.client.get(reverse('weight_converter'))
        self.assertTemplateUsed(response, 'weight_converter.html')

    def test_url_weightconverter_resoves_weight_converter_view(self):
        view = resolve('/weight_converter/')
        self.assertEqual(view.func.__name__, 'weight_converter')













