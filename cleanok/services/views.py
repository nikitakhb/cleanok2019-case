from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Service, ServiceCategory, WorkItem
from .serializers import ServiceCategorySerializer, ServiceSerializer
from .serializers import ServiceListSerializer, WorkItemSerializer


class ServiceCategory_DetailsViewSet(viewsets.ModelViewSet):
    """API endpoint that returns service categorie details."""

    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceCategory_ListViewSet(viewsets.ModelViewSet):
    """API endpoint that returns services categories."""

    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    """API endpoint that returns serivce."""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WorkItemViewSer(viewsets.ModelViewSet):
    """API endpoint that returns work items."""

    queryset = WorkItem.objects.all()
    serializer_class = WorkItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
