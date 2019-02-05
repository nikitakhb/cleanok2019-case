"""Promotions views."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Promotion
from .serializers import PromotionSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    """API endpoint that returns promotions."""

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
