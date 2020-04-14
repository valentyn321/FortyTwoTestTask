from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from apps.hello.models import Developer


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


class TestModels(TestCase):
    def test_required_fileds(self):
        """Checks, if all required field are present"""
        self.dev1 = Developer.objects.get(id=1)
        fields = Developer._meta.fields
        required_f = []
        required_f_values = []
        for field in fields:  # checks all required fileds
            if not field.blank:
                required_f.append(str(field))
        for field in required_f_values:
            assert(field in self.dev1._meta.fields)