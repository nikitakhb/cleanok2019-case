from rest_framework import viewsets

from .models import Advice
from .serializers import AdviceSerializer


class ListAdvicesView(viewsets.ModelViewSet):
    """API endpoint that returns advices."""

    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
