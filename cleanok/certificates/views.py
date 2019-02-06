from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Certificate
from .serializers import CertificateSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    """API endpoint that returns certificates."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
