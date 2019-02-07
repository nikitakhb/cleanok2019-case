from rest_framework import serializers

from .models import Album, Picture


class PictureSerializer(serializers.ModelSerializer):
    """Picture serializer."""

    class Meta:
        """Picture serializer fields."""

        model = Picture
        fields = ('title', 'img')


class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer."""

    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        """Album serializer fields."""

        model = Album
        fields = ('id', 'title', 'cover', 'pictures')
