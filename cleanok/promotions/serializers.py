from .models import *
from rest_framework import serializers


class DateField(serializers.RelatedField):

    def to_representation(self, value):
        return value.strftime('%d/%m/%Y')


class PromotionSerializer(serializers.ModelSerializer):
    date = DateField(source='date_publication', many=False, read_only=True)
    title = serializers.CharField(source='name')
    preview = serializers.CharField(source='description')
    text = serializers.SerializerMethodField('get_empty_text')

    class Meta:
        model = Promotion
        fields = ('id', 'date', 'title', 'preview', 'text')

    def get_empty_text(self, obj):
        return ''
