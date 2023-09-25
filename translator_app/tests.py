from django.test import TestCase
from .models import TranslationLog 
from django.urls import reverse

class TextTranslation(TestCase):
    
    def test_return_data(self):
        data = {'my_textarea': 'hey there', 'language_initial': 'hi'}
        expected_output = "सुनो"
        response = self.client.post(reverse('translator_url'), data)
        self.assertEqual(response.status_code, 200)
        current_inst = TranslationLog.objects.all()[0]
        self.assertEqual(data["my_textarea"], current_inst.input_text)
        self.assertEqual(expected_output, current_inst.output_text)
        self.assertEqual(data["language_initial"], current_inst.language_used)