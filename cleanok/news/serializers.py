from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """News serializer."""

    class Meta:
        """News serializer fields."""

        model = News
        fields = ('id', 'date', 'title', 'preview', 'text', 'related')
