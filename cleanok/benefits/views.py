from rest_framework import viewsets

from .models import Benefit
from .serializers import BenefitSerializer


class ListBenefitsView(viewsets.ModelViewSet):
    """API endpoint that returns benefits."""

    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
