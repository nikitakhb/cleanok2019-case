from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News
from .serializers import NewsSerializer


class ListNewsView(viewsets.ModelViewSet):
    """API endpoint that returns news."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = News.objects.filter(date__isnull=False)
    serializer_class = NewsSerializer
