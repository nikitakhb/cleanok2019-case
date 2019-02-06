from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Advice
from .serializers import AdviceSerializer


class ListAdvicesView(viewsets.ModelViewSet):
    """API endpoint that returns advices."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
