# Generated by Django 4.2.2 on 2023-06-21 18:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=512)),
                ("body", models.TextField()),
                (
                    "access_path",
                    models.CharField(
                        blank=True, max_length=512, null=True, unique=True
                    ),
                ),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-pub_date"],
            },
        ),
    ]
