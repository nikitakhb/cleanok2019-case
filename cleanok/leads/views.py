from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Lead
from .serializers import LeadSerializer


class LeadsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
