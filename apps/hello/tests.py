from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from apps.hello.models import Developer


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class TestViews(TestCase):
    """Creats a new user for check, after that, compare with response"""
    def setUp(self):
        """creats"""
        self.dev1 = Developer.objects.get(id=1)

    def test_contacts_view(self):
        """compare"""
        client = Client()
        response = client.get(reverse('main'))
        self.assertTemplateUsed(response, 'hello/developer_detail.html')
        self.assertContains(response, self.dev1.name)
        self.assertContains(response, self.dev1.last_name)
        self.assertContains(response, self.dev1.email)
        self.assertContains(response, self.dev1.jabber)


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
