from rest_framework import serializers

from .models import Benefit


class BenefitSerializer(serializers.ModelSerializer):
    """Benefit serializer."""

    class Meta:
        """Benefit serializer fields."""

        model = Benefit
        fields = ('title', 'content', 'img')
