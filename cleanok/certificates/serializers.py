from .models import *
from rest_framework import serializers


class UrlField(serializers.RelatedField):
    def to_representation(self, value):
        return value.url


class CertificateSerializer(serializers.ModelSerializer):
    url = UrlField(source='image', many=False, read_only=True)
    title = serializers.CharField(source='name')
    subt = serializers.CharField(source='company')

    class Meta:
        model = Certificate
        fields = ('url', 'title', 'subt')
