from .models import *
from rest_framework import serializers


class DateField(serializers.RelatedField):

    def to_representation(self, value):
        return value.strftime('%d/%m/%Y')


class PromotionSerializer(serializers.ModelSerializer):
    date_publication = DateField(many=False, read_only=True)

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'description', 'date_publication')
