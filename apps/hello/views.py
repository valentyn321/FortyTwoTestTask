from apps.hello.models import Developer
from django.views.generic import DetailView


class ContactsDetailView(DetailView):
    model = Developer

    def get_object(self):
        return Developer.objects.get(pk=1)
