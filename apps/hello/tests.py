from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class TestViews(TestCase):
    def test_contacts_view(self):
        """compare"""
        client = Client()
        response = client.get(reverse('main'))
        self.assertTemplateUsed(response, 'hello/main.html')
        self.assertContains(response, "Valentyn")
        self.assertContains(response, "Cherkasov")
        self.assertContains(response, "vcherkasov321@gmail.com")
        self.assertContains(response, "valentyn17@42cc.co")
