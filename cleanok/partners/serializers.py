from rest_framework import serializers

from .models import PartnerCategory, Partner


class PartnerSerializer(serializers.ModelSerializer):
    """Partner serializer."""

    class Meta:
        """Partner serializer fields."""

        model = Partner
        fields = ('name', 'img')


class PartnerCategorySerializer(serializers.ModelSerializer):
    """Partner category serializer."""

    list = PartnerSerializer(source='partners', many=True, read_only=True)

    class Meta:
        """Partner category serializer fields."""

        model = PartnerCategory
        fields = ('name', 'list')
