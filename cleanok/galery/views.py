from rest_framework import generics
from .models import Album, Picture
from .serializers import AlbumSerializer, PictureSerializer


class ListAlbumsView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ListPicturesView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
