from rest_framework import serializers
from .models import Album, Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('title', 'picture')


class AlbumSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('title', 'picture', 'pictures')
