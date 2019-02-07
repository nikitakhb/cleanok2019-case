from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News
from .serializers import NewsSerializer, SingleNewsSerializer


class NewsViewSet(ModelViewSet):
    """API endpoint that returns news."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = News.objects.filter(date__isnull=False)
    serializer_class = NewsSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = SingleNewsSerializer
        return super(NewsViewSet, self).retrieve(request, *args, **kwargs)
