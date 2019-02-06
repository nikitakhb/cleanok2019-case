from rest_framework import serializers

from .models import Promo


class DateField(serializers.RelatedField):
    """Date serializer."""

    def to_representation(self, value):
        return value.strftime('%d/%m/%Y')


class PromoSerializer(serializers.ModelSerializer):
    """Promo serializer."""

    date = DateField(many=False, read_only=True)

    class Meta:
        """Promo serializer fields."""

        model = Promo
        fields = ('id', 'date', 'title', 'preview', 'text')
