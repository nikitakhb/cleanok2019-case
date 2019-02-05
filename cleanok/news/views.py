from rest_framework import viewsets
from .models import News

from .serializers import NewsSerializer


class ListNewsView(viewsets.ModelViewSet):
    """API endpoint that returns news."""

    queryset = News.objects.filter(date__isnull=False)
    serializer_class = NewsSerializer
