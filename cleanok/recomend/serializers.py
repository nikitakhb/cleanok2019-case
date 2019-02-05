"""Recommend serializers."""

from rest_framework import serializers

from .models import Recomend


class RecomendSerializer(serializers.ModelSerializer):
    """Recomend serializer."""

    class Meta:
        """Recomend serializer fields."""

        model = Recomend
        fields = ('title', 'subt', 'url')
