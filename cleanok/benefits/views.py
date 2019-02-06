from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Benefit
from .serializers import BenefitSerializer


class ListBenefitsView(viewsets.ModelViewSet):
    """API endpoint that returns benefits."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
