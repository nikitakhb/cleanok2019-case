from rest_framework import serializers
from .models import PartnerCategory, Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('name', 'img')


class PartnerCategorySerializer(serializers.ModelSerializer):
    list = PartnerSerializer(source='partners', many=True, read_only=True)

    class Meta:
        model = PartnerCategory
        fields = ('name', 'list')
