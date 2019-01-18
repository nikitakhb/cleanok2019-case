from django.shortcuts import render
from .models import *
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *


# Create your views here.

class VacancyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
