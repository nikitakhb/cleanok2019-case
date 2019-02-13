from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import FeedBackMessage
from .serializers import FeedBackMessageSerializer


class FeedBackMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    queryset = FeedBackMessage.objects.all()
    serializer_class = FeedBackMessageSerializer
