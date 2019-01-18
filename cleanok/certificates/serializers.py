from .models import *
from rest_framework import serializers


class ImageField(serializers.RelatedField):

    def to_representation(self, value):
        return {
            'url': value.url,
            'height': value.height,
            'width': value.width
        }


class CertificateSerializer(serializers.ModelSerializer):

    image = ImageField(many=False, read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'name', 'company', 'image')
