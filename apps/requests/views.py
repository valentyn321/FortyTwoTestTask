from apps.requests.models import Http_Request
from django.views.generic import ListView


class RequestsListView(ListView):
    model = Http_Request
    template_name = 'requests/requests.html'

    def get_queryset(self, **kwargs):
            qs = super(RequestsListView, self).get_queryset(**kwargs)
            return qs.order_by("-id")[:10]
