from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TypeContactSerializer
from .models import TypeContact


class ContactsViewSet(viewsets.ModelViewSet):
    """API endpoint that returns contacts."""

    queryset = TypeContact.objects.all()
    serializer_class = TypeContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        response = super(ContactsViewSet, self).list(request, *args, **kwargs)
        resp = {}
        for key, value in response.data['results']:
            resp[key] = value
        response.data['results'] = resp
        return response
