from rest_framework import generics

from pictures.models import Picture
from pictures.serializers import PictureShortSerializer


class PictureListAPIView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureShortSerializer
