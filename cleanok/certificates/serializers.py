from rest_framework import serializers

from .models import Certificate


class UrlField(serializers.RelatedField):
    """UrlField serializer."""

    def to_representation(self, value):
        return value.url


class CertificateSerializer(serializers.ModelSerializer):
    """Certificate serializer."""

    url = UrlField(source='image', many=False, read_only=True)
    title = serializers.CharField(source='name')
    subt = serializers.CharField(source='company')

    class Meta:
        """Certificate serializer fields."""

        model = Certificate
        fields = ('url', 'title', 'subt')
