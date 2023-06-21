from django.db.models import Q
from django.http import Http404
from rest_framework import generics

from news.models import Article
from news.serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all().exclude(access_path__isnull=False)
    serializer_class = ArticleListSerializer


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get_object(self):
        # Check if access_path is an uuid
        if len(self.kwargs["access_path"]) == 36:
            qs = self.get_queryset().filter(id=self.kwargs["access_path"])

        else:
            qs = self.get_queryset().filter(access_path=self.kwargs["access_path"])

        obj = qs.first()

        if not obj:
            raise Http404

        return obj
