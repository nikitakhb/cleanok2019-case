from django.shortcuts import render
from .models import *
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *


# Create your views here.

class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
