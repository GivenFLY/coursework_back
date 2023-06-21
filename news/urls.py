from django.urls import path

from news.views import ArticleListAPIView, ArticleDetailAPIView

urlpatterns = [
    path("", ArticleListAPIView.as_view()),
    path("<str:access_path>/", ArticleDetailAPIView.as_view()),
]
