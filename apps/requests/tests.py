from django.test import TestCase
from apps.requests.models import Http_Request
from django.core.exceptions import ValidationError
from apps.requests.middleware import StoreRequestMiddleware
from mock import Mock


class TestModels(TestCase):
    def setUp(self):
        '''Creats a new requests for check, second is not valid'''
        self.http1 = Http_Request.objects.create(
            request_method='POST',
            server_name='localhost',
            request_body='some_large_body',
            request_path='/',
            time_of_request="10:10:10"
        )

        self.http2 = Http_Request.objects.create(
            request_method='INCORRECT_METHOD',
            server_name='localhost',
            request_body='some_large_body',
            request_path='/',
            time_of_request="10:10:12"
        )

    def test_model_http(self):
        """Django doesn't do model-level validation of the length and
        SQLite does not enforce lengths on varchar fields. So we have to do
        this manually"""
        query = Http_Request.objects.all()
        for obj in query:
            try:
                obj.full_clean()
            except ValidationError:
                print("Validation Error! Check fileds of you model!")
                Http_Request.objects.get(id=obj.id).delete()
        self.assertEquals(Http_Request.objects.count(), 1)


class StoreRequestMiddlewareTests(TestCase):
    def setUp(self):
        """Here we using Mock"""
        self.middleware = StoreRequestMiddleware()
        self.request = Mock()
        self.request.META = {
            "SERVER_NAME": 'localhost'
        }
        self.request.path = '/testURL/'
        self.request.body = ''
        self.request.method = "GET"

    def test_requestProcessing(self):
        """Comparing"""
        response = self.middleware.process_request(self.request)
        self.assertIsNone(response)
        count = Http_Request.objects.all().count()
        self.assertEqual(count, 1)
