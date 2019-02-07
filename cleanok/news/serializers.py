from rest_framework.serializers import ModelSerializer

from .models import News


class RelatedNewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'date', 'title', 'preview')


class SingleNewsSerializer(ModelSerializer):

    related = RelatedNewsSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'date', 'title', 'text', 'preview', 'related')


class NewsSerializer(ModelSerializer):
    """News serializer."""

    related = RelatedNewsSerializer(many=True, read_only=True)

    class Meta:
        """News serializer fields."""

        model = News
        fields = ('id', 'date', 'title', 'preview', 'related')
        depth = 1
