from django.shortcuts import render
from .models import *
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *


# Create your views here.

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceViewSer(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WorkItemViewSer(viewsets.ModelViewSet):
    queryset = WorkItem.objects.all()
    serializer_class = WorkItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
