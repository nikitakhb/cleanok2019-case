from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer


class ListNewsView(viewsets.ModelViewSet):
    queryset = News.objects.filter(published_date__isnull=False)
    serializer_class = NewsSerializer
