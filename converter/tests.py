from django.test import TestCase
from django.urls import reverse, resolve


class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_converter_page_status_code(self):
        response = self.client.get('/converter/')
        self.assertEqual(response.status_code, 200)

    def test_url_home_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')

    def test_url_converter_by_name(self):
        response = self.client.get(reverse('converter'))
        self.assertTemplateUsed(response, 'converter.html')

    def test_url_converter_resolves_weight_converter_view(self):
        view = resolve(reverse('converter'))
        self.assertEqual(view.func.__name__, 'converter')

    def test_converter_view_calculation(self):
        response = self.client.post(reverse('converter'), {'added_data': '1234',
                                                   'selected_converter': 'weight_converter'})
        self.assertEqual(response.context['result'], 1.234)















