from rest_framework import serializers

from .models import Promotion


class DateField(serializers.RelatedField):
    """Date serializer."""

    def to_representation(self, value):
        return value.strftime('%d/%m/%Y')


class PromotionSerializer(serializers.ModelSerializer):
    """Promotion serializer."""

    date = DateField(source='date_publication', many=False, read_only=True)
    title = serializers.CharField(source='name')
    preview = serializers.CharField(source='description')
    text = serializers.SerializerMethodField('get_empty_text')

    class Meta:
        """Promotion serializer fields."""

        model = Promotion
        fields = ('id', 'date', 'title', 'preview', 'text')

    def get_empty_text(self, obj):
        return ''
