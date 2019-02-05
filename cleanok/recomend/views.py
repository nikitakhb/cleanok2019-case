"""Recomend views."""

from rest_framework import viewsets

from .models import Recomend
from .serializers import RecomendSerializer


class ListRecomendsView(viewsets.ModelViewSet):
    """API endpoint that returns recomendations."""

    queryset = Recomend.objects.all()
    serializer_class = RecomendSerializer
