from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail

class IndexViewTestCase (TestCase):

    def setUp (self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown (self):
        pass

    def test_status_code (self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_tempate_used (self):
        response = self.client.get (self.url)
        self.assertTemplateUsed(response, 'index.html')

class ContactViewTestCase (TestCase):

    def setUp (self):
        self.client = Client()
        self.url = reverse('contact')

    def test_view_ok(self):
        response = self.client.get (self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error (self):
        data = {'name': '', 'message': '', 'email': ''}
        response = self.client.post(self.url, data)
        self.assertFormError (response, 'forms', 'name', 'Este campo é obrigatório.')
        self.assertFormError (response, 'forms', 'email', 'Este campo é obrigatório.')
        self.assertFormError (response, 'forms', 'message', 'Este campo é obrigatório.')

    def test_form_ok (self):
        data = {'name': 'test', 'message': 'test', 'email': 'test@test.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['sucess'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do Django E-Commerce')