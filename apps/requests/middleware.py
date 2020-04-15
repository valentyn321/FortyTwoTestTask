from apps.requests.models import Http_Request
from datetime import datetime


class StoreRequestMiddleware(object):
    def process_request(self, request):
        Http_Request.objects.create(
            request_method=request.method,
            server_name=request.META["SERVER_NAME"],
            request_body=request.body,
            request_path=request.path,
            time_of_request=datetime.now().strftime("%H:%M:%S")
        )
