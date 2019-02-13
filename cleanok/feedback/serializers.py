from rest_framework.serializers import ModelSerializer

from .models import FeedBackMessage


class FeedBackMessageSerializer(ModelSerializer):

    class Meta:
        model = FeedBackMessage
        fields = ('id', 'first_name', 'last_name', 'message')
