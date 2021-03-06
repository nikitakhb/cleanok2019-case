from rest_framework import serializers

from .models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    """Certificate serializer."""

    title = serializers.CharField(source='name')
    subt = serializers.CharField(source='company')
    url = serializers.ImageField(source='image')

    class Meta:
        """Certificate serializer fields."""

        model = Certificate
        fields = ('url', 'title', 'subt')
