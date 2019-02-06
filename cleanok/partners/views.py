from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Partner, PartnerCategory
from .serializers import PartnerSerializer, PartnerCategorySerializer


class ListPartnerCategoriesView(viewsets.ModelViewSet):
    """API endpoint that returns partners categories."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = PartnerCategory.objects.all()
    serializer_class = PartnerCategorySerializer


class ListPartnersView(viewsets.ModelViewSet):
    """API endpoint that returns partners."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
