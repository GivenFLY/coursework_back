from django.urls import path

from pictures.views import PictureListAPIView

urlpatterns = [
    path("", PictureListAPIView.as_view()),
]
