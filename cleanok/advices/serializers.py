from .models import Advice

from rest_framework import serializers


class AdviceSerializer(serializers.ModelSerializer):
    """Advice serializer."""

    class Meta:
        """Advice serializer fields."""

        model = Advice
        fields = ['title', 'text', 'link']
