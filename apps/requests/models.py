from django.db import models
from datetime import datetime


class Http_Request(models.Model):
    request_method = models.CharField(max_length=7)
    server_name = models.CharField(max_length=128)
    request_body = models.CharField(max_length=256)
    request_path = models.CharField(max_length=256)
    time_of_request = models.TimeField(
        default=datetime.now().strftime("%H:%M:%S"),
    )
    read = models.BooleanField(default=False)
