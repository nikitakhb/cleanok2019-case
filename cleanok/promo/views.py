"""Promo views."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Promo
from .serializers import PromoSerializer


class PromoViewSet(viewsets.ModelViewSet):
    """API endpoint that returns promotions."""

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
