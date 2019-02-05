from rest_framework import viewsets

from .models import Partner, PartnerCategory
from .serializers import PartnerSerializer, PartnerCategorySerializer


class ListPartnerCategoriesView(viewsets.ModelViewSet):
    """API endpoint that returns partners categories."""

    queryset = PartnerCategory.objects.all()
    serializer_class = PartnerCategorySerializer


class ListPartnersView(viewsets.ModelViewSet):
    """API endpoint that returns partners."""

    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
