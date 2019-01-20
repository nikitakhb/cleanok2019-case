from rest_framework import generics
from .models import News
from .serializers import NewsSerializer


class ListNewsView(generics.ListAPIView):
    queryset = News.objects.filter(published_date__isnull=False)
    serializer_class = NewsSerializer
