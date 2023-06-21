from rest_framework import serializers

from news.models import Article
from pictures.serializers import PictureShortSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    picture = PictureShortSerializer()

    class Meta:
        model = Article
        fields = ("id", "title", "picture", "pub_date")


class ArticleDetailSerializer(serializers.ModelSerializer):
    picture = PictureShortSerializer()

    class Meta:
        model = Article
        fields = ("id", "title", "body", "picture", "pub_date")
