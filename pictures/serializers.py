from rest_framework import serializers

from pictures.models import Picture


class PictureShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "title", "contents")


class PictureFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "title", "contents", "pub_date")
        read_only_fields = ("pub_date",)
