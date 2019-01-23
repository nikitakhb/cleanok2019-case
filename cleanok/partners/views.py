from rest_framework import viewsets
from .models import Partner, PartnerCategory
from .serializers import PartnerSerializer, PartnerCategorySerializer


class ListPartnerCategoriesView(viewsets.ModelViewSet):
    queryset = PartnerCategory.objects.all()
    serializer_class = PartnerCategorySerializer


class ListPartnersView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
