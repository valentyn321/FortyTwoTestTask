from apps.hello.models import Developer
from apps.requests.models import Http_Request
from django.views.generic import DetailView


class ContactsDetailView(DetailView):
    model = Developer

    def get_object(self):
        return Developer.objects.get(pk=1)

    def get_context_data(self, **kwargs):
        data = super(ContactsDetailView, self).get_context_data(**kwargs)
        https = Http_Request.objects.all().order_by("-id")[:10]
        data['object_list'] = https
        return data
