"""Recomend views."""

from rest_framework import viewsets

from .models import Recomend
from .serializers import RecomendSerializer


class ListRecomendsView(viewsets.ModelViewSet):
    queryset = Recomend.objects.all()
    serializer_class = RecomendSerializer
