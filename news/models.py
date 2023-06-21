import uuid

from django.db import models


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=512)

    picture = models.ForeignKey(
        "pictures.Picture", on_delete=models.SET_NULL, null=True, blank=True
    )

    body = models.TextField()

    access_path = models.CharField(max_length=512, unique=True, null=True, blank=True)

    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-pub_date"]
