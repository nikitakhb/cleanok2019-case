from rest_framework import viewsets
from .models import Album, Picture
from .serializers import AlbumSerializer, PictureSerializer


class ListAlbumsView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ListPicturesView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
