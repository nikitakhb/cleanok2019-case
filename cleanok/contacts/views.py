from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *

# Create your views here.

class ContactsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TypeContact.objects.all()
    serializer_class = TypeContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        response = super(ContactsViewSet, self).list(request, *args, **kwargs)
        resp = {}
        for key, value in response.data:
            print(f'[{key}] = {value}')
            resp[key] = value

        response.data = resp
        return response

